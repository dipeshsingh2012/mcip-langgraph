# Multi-Agent Clinical Intelligence Platform (MCIP)

**A LangGraph-powered multi-agent system for hospital workflow optimization on GCP**

## Project Overview

Build a **stateful, production-ready multi-agent platform** using **LangGraph** to assist hospital teams with clinical decision support, documentation, triage, and administrative tasks. The system emphasizes reliability, auditability, and human oversight — critical for healthcare.

**Ideal for**: MTech thesis, internal hospital tool, portfolio showcase.

**Key Features**:
- Multi-agent collaboration orchestrated by LangGraph
- Persistent state & checkpointing per patient case
- Human-in-the-loop at critical points
- Grounded RAG on medical knowledge
- GCP-native deployment with Vertex AI Gemini models
- Compliance-focused design (HIPAA considerations)

## Architecture

### Agents (Graph Nodes)
1. **Intake & Triage Agent** — Processes incoming data
2. **Evidence Research Agent** — RAG over guidelines & literature
3. **Diagnosis Support Agent** — Differential diagnosis
4. **Care Plan Agent** — Treatment recommendations
5. **Documentation Agent** — Note generation
6. **Compliance Agent** — Risk & privacy checks
7. **Coordinator Agent** — Orchestration & routing
8. **Human Review Node** — Approval gates

### Core Technologies
- **LangGraph + LangChain**: Core orchestration
- **Vertex AI (Gemini)**: Primary LLM
- **Vector Search**: RAG
- **Cloud Run / GKE**: Deployment
- **LangSmith**: Observability
- **Pub/Sub + Logging**: Eventing & monitoring

## Project Phases & Timeline

### Phase 1: Foundation & MVP (1-2 months)
- Basic LangGraph setup with Vertex AI
- Simple linear graph (Intake → Research → Summary)
- RAG pipeline
- Basic API/UI

**Milestone**: Working end-to-end prototype on synthetic data.

### Phase 2: Multi-Agent Expansion (2-5 months)
- Full agent team
- Complex graph with branches & loops
- Memory & state management
- Evaluation framework

**Milestone**: Multi-agent collaboration with human review.

### Phase 3: Production Hardening (5-9 months)
- Security, auditing, error handling
- Advanced integrations (FHIR if available)
- Monitoring & reliability
- Compliance documentation

**Milestone**: Deployable version ready for internal pilot (de-identified).

### Phase 4: Research & Extension (9+ months)
- Multimodal support
- Adaptive learning from feedback
- Thesis writing, paper submission
- Potential hospital deployment

## Getting Started

### Prerequisites
- Python 3.10+
- GCP Project with Vertex AI enabled
- Service account with Vertex AI, Storage, Logging permissions

### Installation

```bash
git clone <your-repo>
cd mcip-langgraph
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Project Structure

```
mcip-langgraph/
├── agents/                 # Individual agent logic
├── graph/                  # State, builder, nodes
├── tools/                  # Custom tools
├── rag/                    # Vector store & retrievers
├── config/                 # Settings & prompts
├── deployment/             # GCP configs
├── evaluation/             # Metrics & testing
├── main.py
├── README.md
└── requirements.txt
```

### Core Code Skeletons

**1. State Definition (`graph/state.py`)**

```python
from typing import TypedDict, Annotated, List, Optional
from langgraph.graph.message import add_messages
from pydantic import BaseModel

class PatientCase(BaseModel):
    patient_id: str
    symptoms: List[str] = []
    medical_history: str = ""
    current_medications: List[str] = []
    lab_results: str = ""
    messages: Annotated[list, add_messages] = []
    current_diagnosis: Optional[str] = None
    care_plan: Optional[str] = None
    status: str = "in_progress"
    needs_human_review: bool = False
    audit_log: List[str] = []
```

**2. Main Graph Builder** — Use Copilot to expand this.

## Safety & Ethics Guidelines
- Always route final clinical decisions to licensed professionals.
- Use synthetic or fully de-identified data for development.
- Implement output guardrails.
- Maintain full audit trails.

## Resources
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai)
- LangSmith for tracing

---

**Start Building**: Open files in VS Code with GitHub Copilot enabled. Ask Copilot to "Implement the Intake Agent using LangGraph node" etc.

This README serves as your living project bible. Update it as you progress.

**Next Immediate Step**: Set up the basic LangGraph + Vertex AI "Hello World" graph.
