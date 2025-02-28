import os
from autogen import ConversableAgent
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch


llm_config = {
    "model": "gemini-2.0-flash",
    "api_type": "google",
    "api_key": os.environ["GOOGLE_GENAI_API_KEY"]
}

client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])

google_search_tool = Tool(
    google_search=GoogleSearch()
)


def get_content(question: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question,
        config=GenerateContentConfig(
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )
    return response.text


get_content_agent = ConversableAgent(
    name="get_content_agent",
    llm_config=llm_config,
    system_message="You are an information retrieval agent. Your primary task is to receive a topic from the user and provide accurate and comprehensive information about it.",
)

executor_agent = ConversableAgent(
    name="executor_agent",
    human_input_mode="NEVER",
)
