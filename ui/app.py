from google.genai import types
import gradio as gr
from google import genai
import soundfile as sf
import io
import os


client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])

ui_blocks = gr.Blocks()


def ask_llm(audio_bytes):
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type='audio/wav',
            ),
            'Answer the next question of the audio',
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
    audio_bytes = get_audio_bytes(audio)
    response = ask_llm(audio_bytes)
    print(response)
    return response


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
            gr.Textbox(label="Ask me",)],
    outputs=[gr.Textbox(label="Response"),],
    allow_flagging="never")

with ui_blocks:
    gr.TabbedInterface(
        [get_prompt_ui_block],
        ["EchoBrief"],
    )

if __name__ == "__main__":
    ui_blocks.launch()
