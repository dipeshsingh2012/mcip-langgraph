# Technical Design Document (TDD)

**Project Name:** Multi-Agent Clinical Intelligence Platform (MCIP)  
**Version:** 1.0  
**Date:** July 06, 2026  
**Author:** Grok (Solution Architect)

---

## 1. Introduction

This document provides the detailed technical design for the MVP of MCIP based on the approved High-Level Architecture and MVP Scope.

**Objective**: Give developers clear guidance to implement a reliable, maintainable, and production-ready foundation.

---

## 2. Technology Stack

- **Orchestration**: LangGraph + LangChain
- **LLM**: Gemini via Vertex AI (`ChatVertexAI`)
- **Vector Store**: Vertex AI Vector Search (or pgvector as fallback)
- **State Management**: Pydantic models + LangGraph checkpointing
- **Deployment**: Cloud Run (primary), Vertex AI Agent Engine (future)
- **Observability**: LangSmith + Google Cloud Logging/Monitoring
- **Language**: Python 3.11+

---

## 3. Core Data Model

```python
from pydantic import BaseModel
from typing import List, Optional, Annotated
from langgraph.graph.message import add_messages

class PatientCase(BaseModel):
    patient_id: str
    symptoms: List[str] = []
    medical_history: str = ""
    current_medications: List[str] = []
    lab_results: str = ""
    messages: Annotated[list, add_messages] = []
    draft_note: Optional[str] = None
    discharge_summary: Optional[str] = None
    compliance_flags: List[str] = []
    status: str = "in_progress"          # in_progress, review, approved, rejected
    needs_human_review: bool = True
    audit_log: List[str] = []
    timestamp: str = ""
```

---

## 4. LangGraph Design

**Main Graph Structure**:
- **Supervisor Node** (Coordinator Agent) — decides next step
- **Agent Nodes**: Intake, Research, Documentation, Compliance
- **Human Review Node** — conditional pause
- **End Node**

**Key Features**:
- Persistent checkpointing (save/resume per patient case)
- Conditional routing
- Memory (short-term + long-term via RAG)

---

## 5. Agent Specifications

**1. Intake Agent**
- Responsibility: Parse and structure incoming patient data
- Tools: None initially

**2. Research Agent**
- Responsibility: Retrieve relevant medical knowledge using RAG
- Tools: Vector Search retriever

**3. Documentation Agent**
- Responsibility: Generate clinical note and discharge summary
- Tools: None

**4. Compliance Agent**
- Responsibility: Check for privacy, billing, risk flags
- Tools: Rule-based + LLM checks

**5. Coordinator Agent**
- Responsibility: Overall flow control and decision making

---

## 6. RAG Architecture

- Document Loader → Text Splitter → Embeddings (Vertex AI) → Vector Store
- Initial knowledge base: Hospital protocols + public medical guidelines (de-identified)
- Retrieval: Top-k + reranking (future)

---

## 7. Human-in-the-Loop Design

- Use LangGraph’s `interrupt_before` or custom node
- Store state and notify doctor via email/API
- Resume graph after approval/rejection with feedback

---

## 8. Project Structure

```
mcip-langgraph/
├── agents/                  # Each agent as a module
├── graph/
│   ├── state.py
│   ├── builder.py
│   ├── nodes.py
│   └── workflow.py
├── rag/
├── tools/
├── config/
├── deployment/
├── evaluation/
├── main.py
├── requirements.txt
└── README.md
```

---

## 9. Security & Compliance

- Use service accounts with least privilege
- Encrypt data in transit and at rest
- Log all agent decisions
- No PHI in prompts during development

---

## 10. Testing Strategy

- Unit tests for individual nodes
- Integration tests for graph execution
- Clinical accuracy evaluation (doctor review)
- Load & reliability testing

---

## 11. Next Steps After This Document

1. Repository initialization
2. Implement core graph skeleton
3. Build first agent (Intake)
4. Integrate Vertex AI
5. Weekly demos

---

**Prepared by:** Grok (Solution Architect)  
**Date:** July 06, 2026
