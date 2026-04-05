from pipelines.streaming_simulator import stream_data
from orchestrator.graph import build_graph
import time

def main():
    app = build_graph()

    while True:
        data = stream_data()

        state = {
            "data": data,
            "dq_issues": [],
            "risk_issues": [],
            "root_cause": "",
            "decision": ""
        }

        result = app.invoke(state)

        print("\n=== NEW BATCH (LangGraph) ===")
        print("DQ Issues:", result["dq_issues"])
        print("Risk Issues:", result["risk_issues"])
        print("Root Cause:", result["root_cause"])
        print("Decision:", result["decision"])

        time.sleep(3)

if __name__ == "__main__":
    main()