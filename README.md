# Rule-Based Risk Monitor

A rule-based, multi-agent system that continuously monitors, validates, and explains data quality and risk signals in near real-time — aligned with **BCBS 239** principles for risk data aggregation and reporting.

Built using **LangGraph** for agent orchestration, this system simulates a streaming financial transaction pipeline and runs four sequential agents to detect issues, identify root causes, and make actionable decisions.

---

## Architecture

![High Level Architecture](/screenshots/hla.png)
Streaming Data (pipelines/)
↓
[DQ Agent] → [Risk Agent] → [RCA Agent] → [Decision Agent]
↑__________LangGraph StateGraph (orchestrator/)↑



Each agent in the pipeline receives shared state and contributes its findings before passing control to the next node.

---

## Agents

| Agent | File | Responsibility |
|---|---|---|
| **Data Quality Agent** | `agents/dq_agent.py` | Detects null values, empty batches, and unusually high average transaction amounts |
| **Risk Agent** | `agents/risk_agent.py` | Flags high transaction volatility (std > 7000) and potential fraud (max > 18,000) |
| **Root Cause Analysis Agent** | `agents/rca_agent.py` | Classifies root cause as pipeline/ingestion issue or abnormal transaction behavior |
| **Decision Agent** | `agents/decision_agent.py` | Emits `ALERT` if any DQ or risk issue exists, otherwise `IGNORE` |

---

## Project Structure

rule-based-risk-monitor/
│
├── agents/
│ ├── dq_agent.py # Data Quality checks
│ ├── risk_agent.py # Risk signal detection
│ ├── rca_agent.py # Root Cause Analysis
│ └── decision_agent.py # Final decision emitter
│
├── orchestrator/
│ ├── graph.py # LangGraph StateGraph definition
│ ├── nodes.py # Node wrappers for each agent
│ └── state.py # Shared AgentState schema
│
├── pipelines/
│ └── streaming_simulator.py # Simulates streaming transaction batches
│
├── main.py # Entry point — runs the monitoring loop
├── requirements.txt
└── README.md


---

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/jainparag1/rule-based-risk-monitor.git
cd rule-based-risk-monitor
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

The system will continuously stream simulated transaction batches every 3 seconds, process them through the agent graph, and print findings to the console.

### Sample Output

=== NEW BATCH (LangGraph) ===
DQ Issues: ['Unusually high average transaction value']
Risk Issues: ['High transaction volatility', 'Potential high-value fraud transaction']
Root Cause: Abnormal transaction behavior detected
Decision: ALERT


---

## Rule Definitions

### Data Quality Rules
- **Null Check** — Flags if any null values are present in the batch
- **High Average Amount** — Flags if mean transaction amount exceeds $15,000
- **Empty Batch** — Flags if no transactions are received

### Risk Rules
- **High Volatility** — Flags if standard deviation of amounts exceeds $7,000
- **Fraud Threshold** — Flags if any single transaction exceeds $18,000

---

## BCBS 239 Alignment

This system is designed with BCBS 239 principles in mind:

- **Accuracy & Integrity** — DQ agent enforces data completeness and plausibility checks
- **Completeness** — Every batch is evaluated; empty batches are explicitly flagged
- **Timeliness** — Near real-time streaming simulation with 3-second polling intervals
- **Adaptability** — Modular agent design allows rules to be extended independently

---

## Tech Stack

| Component | Technology |
|---|---|
| Agent Orchestration | [LangGraph](https://github.com/langchain-ai/langgraph) |
| Data Processing | Pandas, NumPy |
| Streaming Simulation | Python `random` + Pandas |
| UI (optional) | Streamlit |
| Vector Store (optional) | FAISS |

---

## Roadmap

- [ ] Add Streamlit dashboard for real-time visualization
- [ ] Integrate LLM-based explanations for root cause summaries
- [ ] Add configurable rule thresholds via YAML/env
- [ ] Connect to real Kafka stream instead of simulator
- [ ] Persist alerts to a database or S3

---

## License

MIT
