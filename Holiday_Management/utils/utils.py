from autogen_agentchat.conditions import TextMentionTermination

from autogen_agentchat.conditions import MaxMessageTermination

def get_termination_condition():
    """
        Get the termination condition for the agent
    """
    return MaxMessageTermination(max_messages=6)