import io
import json
import os

import gradio as gr
import soundfile as sf
from blogging_agent import blogging_agent
from create_images_agent import create_image_agent
from dotenv import load_dotenv
from get_content_agent import get_content_agent
from google import genai
from google.genai import types
from sequential_agents import expert_content_agent


load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])

ui_blocks = gr.Blocks()


def trascribe_llm(audio_bytes):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type="audio/wav",
            ),
            "transcribe:",
        ],
    )
    return response.text


def get_audio_bytes(audio):
    sample_rate, data = audio
    with io.BytesIO() as buffer:
        sf.write(buffer, data, sample_rate, format="WAV")
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
            {
                "recipient": create_image_agent,
                "message": "Create an image",
                "max_turns": 2,
                "summary_method": "last_msg",
            },
        ]
    )
    print(results[1].summary)
    print(results[2].summary)
    result = results[1].summary
    lesson_plan_json = json.loads(result)
    return (
        lesson_plan_json["title"],
        lesson_plan_json["text"],
        lesson_plan_json["links"],
        gr.Image("images/image_blog.png"),
    )


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
    inputs=[
        input_audio,
        gr.Textbox(label="Ask me", value="Search about the Mexican animal axolotl"),
    ],
    outputs=[
        gr.Textbox(label="Title"),
        gr.Textbox(label="Text"),
        gr.Textbox(label="Links"),
        gr.Image(),
    ],
    allow_flagging="never",
)

with ui_blocks:
    gr.TabbedInterface(
        [get_prompt_ui_block],
        ["AI-Powered Blog Generator"],
    )

if __name__ == "__main__":
    ui_blocks.launch()
