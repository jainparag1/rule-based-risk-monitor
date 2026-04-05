from agents.dq_agent import dq_agent
from agents.risk_agent import risk_agent
from agents.rca_agent import rca_agent
from agents.decision_agent import decision_agent

def dq_node(state):
    state["dq_issues"] = dq_agent(state["data"])
    return state

def risk_node(state):
    state["risk_issues"] = risk_agent(state["data"])
    return state

def rca_node(state):
    state["root_cause"] = rca_agent(
        state["dq_issues"],
        state["risk_issues"]
    )
    return state

def decision_node(state):
    state["decision"] = decision_agent(
        state["dq_issues"],
        state["risk_issues"]
    )
    return state