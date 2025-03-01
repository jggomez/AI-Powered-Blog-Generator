import os

from autogen import ConversableAgent
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel


load_dotenv()


MODEL_GEMINI = "gemini-2.0-flash"
MODEL_GEMINI_IMAGES = "imagen-3.0-generate-002"


class ImagePrompt(BaseModel):
    prompt: str


llm_config = {
    "model": MODEL_GEMINI,
    "api_type": "google",
    "api_key": os.environ["GOOGLE_GENAI_API_KEY"],
}

client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])


def create_prompt_image(text: str) -> ImagePrompt:
    prompt = f"Create a prompt for creating an image based on this text: {text}"
    response_model = client.models.generate_content(
        model=MODEL_GEMINI,
        contents=prompt,
        config=GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ImagePrompt,
        ),
    )
    return response_model.parsed


def create_image_google(text: str) -> str:
    url_image = "images/image_blog.png"
    prompt = create_prompt_image(text)
    print(prompt.prompt)
    response_model = client.models.generate_images(
        model=MODEL_GEMINI_IMAGES,
        prompt=prompt.prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
        ),
    )
    if len(response_model.generated_images) > 0:
        with open(url_image, "wb") as f:
            f.write(response_model.generated_images[0].image.image_bytes)
    return url_image


def create_image(text: str) -> str:
    url_image = create_image_google(text)
    return url_image


create_image_agent_system_message = """
You are an image-creating agent.
Your primary task is to receive a blog text and create image based on it.
"""

create_image_agent = ConversableAgent(
    name="create_image_agent",
    llm_config=llm_config,
    system_message=create_image_agent_system_message,
)
