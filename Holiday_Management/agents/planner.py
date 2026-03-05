from autogen_agentchat.agents import AssistantAgent
from Holiday_Management.models.gpt_model import model_client

planner_agent = AssistantAgent(
    name="Holiday_Planner",
    description="A Holiday Planner Agent that helps users plan their trips",
    model_client=model_client,
    system_message=" You are a holiday planner agent. Your task is to help users plan their trip by providing information about destinations, itineraries and travel tips"
)

