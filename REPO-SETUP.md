# Repository Setup & Development Plan

**Project Name:** Multi-Agent Clinical Intelligence Platform (MCIP)  
**Repository Name:** `mcip-langgraph`  
**Date:** July 06, 2026

---

## 1. Repository Setup Instructions

### Step 1: Create Repository
- Name: `mcip-langgraph`
- Description: "Multi-Agent Clinical Intelligence Platform using LangGraph + Vertex AI for hospital documentation support"
- Visibility: Private (recommended)
- Add README.md, .gitignore (Python), License (MIT)

### Step 2: Clone & Initial Setup

```bash
git clone <your-repo-url>
cd mcip-langgraph

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Prerequisites:
- Python 3.10+ (3.11 recommended)
- `gcloud` SDK installed for GCP auth and deployment

GCP Authentication (example):

```bash
# activate a service account with the required roles
gcloud auth activate-service-account --key-file=/path/to/key.json
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
gcloud config set project YOUR_PROJECT_ID
```

Final Project Structure

```text
mcip-langgraph/
├── agents/                     # Individual agent logic
│   ├── intake_agent.py
│   ├── research_agent.py
│   ├── documentation_agent.py
│   ├── compliance_agent.py
│   └── coordinator.py
├── graph/
│   ├── state.py                # PatientCase model
│   ├── builder.py              # Main graph construction
│   ├── nodes.py                # Node functions
│   └── workflow.py             # Graph execution logic
├── rag/                        # RAG components
│   ├── vectorstore.py
│   └── retriever.py
├── tools/                      # Custom tools
├── config/
│   ├── settings.py
│   └── prompts.py
├── deployment/
│   └── cloudrun.yaml
├── evaluation/                 # Testing & metrics
├── notebooks/                  # Experiments & spikes
├── main.py                     # Entry point
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

3. Key Files to Create First

requirements.txt
graph/state.py
graph/builder.py
main.py
.env.example


4. Development Workflow (with GitHub Copilot)
Best Practice:

Always keep the TDD and MVP Scope open while coding
Use clear, detailed prompts with Copilot
Commit frequently with meaningful messages
Test each agent/node independently before integrating

Example Copilot Prompts:

"Create PatientCase Pydantic model for LangGraph state"
"Build LangGraph StateGraph with Intake, Research and Documentation nodes"
"Implement Research Agent with Vertex AI RAG retriever"


5. Week 1 Goals (First Sprint)

Set up repository and environment
Implement core PatientCase state
Build basic LangGraph skeleton (happy path)
Integrate Vertex AI Gemini
Create first working end-to-end flow (simple version)
Add basic LangSmith tracing


6. Git Best Practices

Main branch protected
Feature branches: feature/intake-agent, feature/rag-integration
Commit messages: Conventional style (feat:, fix:, docs:)


Next Action: After creating this structure, start with graph/state.py and graph/builder.py.
Prepared by: Grok (Solution Architect)
Date: July 06, 2026