import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search, FunctionTool
from google_devfest_agent.devfest_tools import scrape_devfest_event_details

load_dotenv()

MODEL_NAME = os.getenv("GOOGLE_GENAI_MODEL")

root_agent = LlmAgent(
    name="google_devefest_agent",
    model=MODEL_NAME,
    description="Agent that fetches DevFest schedules, images, and generates social posts.",
    instruction=(
        "You are a helpful DevFest assistant. Use tools to fetch schedules, "
        "search images, or generate social media posts."
    ),
    tools=[scrape_devfest_event_details],
    output_key="devfest_agent_output"
)