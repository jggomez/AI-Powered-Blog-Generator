from dotenv import load_dotenv
from get_content_agent import get_content_agent, get_content
from create_images_agent import create_image_agent, create_image
from autogen import ConversableAgent, register_function
import os

load_dotenv()


llm_config = {
    "model": "gemini-2.0-flash",
    "api_type": "google",
    "api_key": os.environ["GOOGLE_GENAI_API_KEY"]
}

expert_content_message = """
You decide topics and work with an agent for getting realible content, you provide one round of feedback on their content text
Then you will work with a summarization agent to get a final output of the content.
"""

expert_content_agent = ConversableAgent(
    name="expert_content_agent",
    llm_config=llm_config,
    system_message=expert_content_message,
)

register_function(
    get_content,
    caller=get_content_agent,
    executor=expert_content_agent,
    description="Primary task is to receive a topic from the user and provide accurate, concise, and comprehensive information about it.",
)

register_function(
    create_image,
    caller=create_image_agent,
    executor=expert_content_agent,
    description="Primary task is to receive a blog text and create image based on it.",
)
