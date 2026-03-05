from autogen_agentchat.agents import AssistantAgent
from Holiday_Management.models.gpt_model import model_client

researcher_agent = AssistantAgent(
    name="Holiday_Researcher",
    description="A Holiday Researcher Agent that helps users Research their holiday destinations.",
    model_client=model_client,
    system_message=" You are a holiday Researcher agent. Your task is to help users Research about their holiday destinations by providing information about destinations, itineraries and travel tips"
)

