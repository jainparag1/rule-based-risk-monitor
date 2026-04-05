from typing import TypedDict, List

class AgentState(TypedDict):
    data: object
    dq_issues: List[str]
    risk_issues: List[str]
    root_cause: str
    decision: str