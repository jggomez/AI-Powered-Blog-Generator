from dotenv import load_dotenv
load_dotenv()
from get_content_agent import get_content_agent, get_content
from autogen import ConversableAgent, register_function
import os
from summarization_agent import summarization_agent


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

results = expert_content_agent.initiate_chats(
    [
        {
            "recipient": get_content_agent,
            "message": "Let's get reliable information for a blog about the Axolotl animal",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": summarization_agent,
            "message": "Create a summary",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
    ]
)

print(results)
print(results[0].summary)
print(results[1].summary)
