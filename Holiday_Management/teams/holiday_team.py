from autogen_agentchat.teams import RoundRobinGroupChat
from Holiday_Management.agents.planner import planner_agent
from Holiday_Management.agents.researcher import researcher_agent
from Holiday_Management.utils.utils import get_termination_condition

team = RoundRobinGroupChat(
    participants=[planner_agent, researcher_agent],
    termination_condition=get_termination_condition()
)