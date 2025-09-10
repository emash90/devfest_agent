import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search, FunctionTool
from google_devfest_agent.devfest_tools import scrape_devfest_event_details, search_for_devfest_images, generate_social_media_post

load_dotenv()

MODEL_NAME = os.getenv("GOOGLE_GENAI_MODEL")

root_agent = LlmAgent(
    name="google_devefest_agent",
    model=MODEL_NAME,
    description="Agent that fetches DevFest schedules, images, and generates social posts.",
    instruction=(
        "You are a helpful DevFest assistant. "
        "Use tools to fetch event schedules from URLs, "
        "find DevFest images by city, "
        "or generate social media posts."
    ),
    tools=[
        scrape_devfest_event_details,
        search_for_devfest_images,
        generate_social_media_post
    ],
    output_key="devfest_agent_output"
)

if __name__ == "__main__":
    print("🚀 DevFest Agent ready!")
    # Example test
    query = "Generate a social media post for DevFest Nairobi with a summary 'AI and Cloud Talks happening all day!'"
    result = root_agent.run(query)
    print(result)