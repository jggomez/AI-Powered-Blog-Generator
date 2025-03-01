import os
import tweepy
from autogen import ConversableAgent
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


MODEL_GEMINI = "gemini-2.0-flash"


class Entities(BaseModel):
    entities: list[str]


llm_config = {
    "model": MODEL_GEMINI,
    "api_type": "google",
    "api_key": os.environ["GOOGLE_GENAI_API_KEY"],
}

client = genai.Client(api_key=os.environ["GOOGLE_GENAI_API_KEY"])

twitter_api = tweepy.Client(os.environ["BEARER_TOKEN"])


def detect_entities(question: str) -> Entities:
    question = "Detect entities of the question" + question
    response_model = client.models.generate_content(
        model=MODEL_GEMINI,
        contents=question,
        config=GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Entities,
        )
    )
    return response_model.parsed


def get_tweets(topic: str) -> list[str]:
    response = twitter_api.search_recent_tweets(topic, max_results=10)
    tweets = response.data
    return [tweet.text for tweet in tweets]


def get_content_grounding(question: str) -> str:
    question = question + ". Please get text, key_words and links"
    response_model = client.models.generate_content(
        model=MODEL_GEMINI,
        contents=question,
        config=GenerateContentConfig(
            tools=[Tool(google_search=GoogleSearch())],
        )
    )
    return response_model.text


def get_content(question: str) -> str:
    response_content = get_content_grounding(question)
    # entities = detect_entities(question)
    # if len(entities.entities) > 0:
    #    tweets = get_tweets(entities.entities[0])
    #    print(tweets)
    #    for tweet in tweets:
    #        response_content += tweet + "\n"
    return response_content


get_content_agent_system_message = """
You are an information retrieval agent. 
Your primary task is to receive a topic from the user and provide accurate and comprehensive information about it.
"""

get_content_agent = ConversableAgent(
    name="get_content_agent",
    llm_config=llm_config,
    system_message=get_content_agent_system_message,
)
