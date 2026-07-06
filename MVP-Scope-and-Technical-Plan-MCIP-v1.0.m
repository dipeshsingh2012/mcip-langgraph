# MVP Scope & Technical Plan Document

**Project Name:** Multi-Agent Clinical Intelligence Platform (MCIP)  
**Version:** 1.0  
**Date:** July 06, 2026  
**Author:** Grok (Solution Architect)

---

## 1. Executive Summary

This document defines the **Minimum Viable Product (MVP)** for MCIP based on the approved High-Level Architecture.

**MVP Goal**: Deliver a functional, safe, and valuable clinical documentation assistant using LangGraph + Vertex AI within 8–10 weeks.

---

## 2. MVP Objectives

- Build a working multi-agent system that can generate high-quality clinical notes and discharge summaries.
- Demonstrate reliable LangGraph orchestration with human-in-the-loop.
- Validate integration with Vertex AI (Gemini).
- Gather early feedback from clinicians.
- Establish strong foundation for future phases.

---

## 3. In-Scope (MVP)

### Primary Use Case
**Clinical Documentation Assistant** for General Medicine / Internal Medicine.

**Key Features**:
- Accept patient case input (symptoms, history, lab results, notes)
- Perform evidence-based research using RAG
- Generate draft clinical notes and discharge summary
- Flag compliance/risk items
- Route output for human doctor review and approval
- Maintain full audit log of agent actions

### Agents Included
1. Intake & Triage Agent
2. Research & Evidence Agent (RAG)
3. Documentation Agent
4. Compliance & Risk Agent
5. Coordinator / Supervisor Agent
6. Human Review Node

---

## 4. Out-of-Scope (MVP)

- Direct treatment or diagnosis recommendations
- Multimodal input (images, scans)
- Real-time triage or emergency use
- Full EHR bidirectional integration
- Adaptive learning from feedback
- Mobile interface

---

## 5. Technical Scope

- **Core Framework**: LangGraph + LangChain
- **LLM**: Gemini via Vertex AI
- **RAG**: Vertex AI Vector Search (initial knowledge base)
- **State Management**: Persistent PatientCase using Pydantic + checkpointing
- **Deployment**: Cloud Run (with option for Vertex AI Agent Engine)
- **Observability**: LangSmith + Google Cloud Logging
- **Security**: Basic auth + audit logging

---

## 6. Success Criteria

### Functional
- End-to-end flow works from input to approved output
- At least 70% of generated notes rated as "usable" by doctors

### Technical
- LangGraph graph executes reliably with checkpointing
- Human-in-the-loop mechanism works smoothly
- Basic RAG returns relevant medical context

### Business
- Positive feedback from at least 3–5 clinicians
- Measurable time saving demonstrated in pilot

---

## 7. Timeline & Milestones (8–10 weeks)

- **Week 1-2**: Project setup, HLD approval, basic LangGraph + Vertex AI spike
- **Week 3-5**: Core graph + 3 main agents
- **Week 6-7**: RAG implementation + Human Review flow
- **Week 8-9**: Testing, evaluation, UI/API
- **Week 10**: Demo + Feedback session