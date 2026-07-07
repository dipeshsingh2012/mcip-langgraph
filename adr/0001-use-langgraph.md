# ADR 0001: Use LangGraph as the primary orchestration framework

Date: 2026-07-07
Status: Accepted

Context
-------
We need an orchestration framework for multi-agent, stateful LLM workflows that supports durable execution, checkpointing, human-in-the-loop interactions, and production readiness for clinical use.

Decision
--------
Adopt LangGraph (StateGraph) as the primary orchestration framework for MCIP.

Consequences
------------
- Pros: Built-in state management, checkpointing, explicit sequencing of nodes, and production-oriented features that fit the platform's needs.
- Cons: Dependency on `langgraph` API stability; will need minor defensive coding for version differences (e.g., `compile()` → `invoke()` changes).

Alternatives Considered
-----------------------
- Implement a custom orchestrator (rejected: high engineering cost).
- Use a simpler task queue + custom state store (rejected: lacks LLM-centric features).

References
----------
- HLD.md (Key Architecture Decisions)
