from typing import TypedDict, Annotated, List, Union
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    # Annotating with operator.add allows messages to be appended rather than overwritten
    messages: Annotated[List[BaseMessage], operator.add]
    user_history: dict
    risk_score: float
    reasoning: List[str]  # Agents will add their findings here
    human_approved: bool  # For the HITL feature