from langgraph.graph import StateGraph
from orchestrator.state import AgentState
from orchestrator.nodes import dq_node, risk_node, rca_node, decision_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("dq", dq_node)
    graph.add_node("risk", risk_node)
    graph.add_node("rca", rca_node)
    graph.add_node("decision", decision_node)

    graph.set_entry_point("dq")

    graph.add_edge("dq", "risk")
    graph.add_edge("risk", "rca")
    graph.add_edge("rca", "decision")

    graph.set_finish_point("decision")

    return graph.compile()