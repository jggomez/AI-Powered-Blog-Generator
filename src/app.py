from google.genai import types
import gradio as gr
from google import genai
import soundfile as sf
import io
import os
from sequential_agents import expert_content_agent
from dotenv import load_dotenv
from blogging_agent import blogging_agent
from get_content_agent import get_content_agent
import json


load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])

ui_blocks = gr.Blocks()


def trascribe_llm(audio_bytes):
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type='audio/wav',
            ),
            'transcribe:',
        ]
    )
    return response.text


def get_audio_bytes(audio):
    sample_rate, data = audio
    with io.BytesIO() as buffer:
        sf.write(buffer, data, sample_rate, format='WAV')
        audio_bytes = buffer.getvalue()

    return audio_bytes


def orchestration(audio, text):
    if text:
        user_question = text
    else:
        audio_bytes = get_audio_bytes(audio)
        user_question = trascribe_llm(audio_bytes)
    results = expert_content_agent.initiate_chats(
        [
            {
                "recipient": get_content_agent,
                "message": user_question,
                "max_turns": 2,
                "summary_method": "last_msg",
            },
            {
                "recipient": blogging_agent,
                "message": "Create a blog",
                "max_turns": 1,
                "summary_method": "last_msg",
            },
        ]
    )
    result = results[1].summary
    print(result)
    lesson_plan_json = json.loads(result)
    return lesson_plan_json["title"], lesson_plan_json["text"], lesson_plan_json["links"]


input_audio = gr.Audio(
    sources=["microphone"],
    waveform_options=gr.WaveformOptions(
        waveform_color="#01C6FF",
        waveform_progress_color="#0066B4",
        skip_length=2,
        show_controls=False,
    ),
)

get_prompt_ui_block = gr.Interface(
    fn=orchestration,
    inputs=[input_audio,
            gr.Textbox(label="Ask me", value="Search about the Mexican animal axolotl")],
    outputs=[gr.Textbox(label="Title"),
             gr.Textbox(label="Text"),
             gr.Textbox(label="Links"),],
    allow_flagging="never")

with ui_blocks:
    gr.TabbedInterface(
        [get_prompt_ui_block],
        ["EchoBrief"],
    )

if __name__ == "__main__":
    ui_blocks.launch()
