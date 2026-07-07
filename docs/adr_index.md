# ADR Index

This folder contains the project's Architectural Decision Records (ADRs). ADRs document important architectural choices, their rationale, alternatives considered, and consequences.

Current ADRs:

- [ADR 0001: Use LangGraph](../adr/0001-use-langgraph.md)
- [ADR 0002: Primary LLM = Gemini via Vertex AI](../adr/0002-primary-llm-gemini-vertex-ai.md)
- [ADR 0003: Human-in-the-Loop by Default](../adr/0003-human-in-the-loop.md)
- [ADR 0004: RAG-First Approach](../adr/0004-rag-first.md)

ADR Template: [ADR_TEMPLATE.md](../adr/ADR_TEMPLATE.md)

Procedure
---------

1. Create a new ADR file in `adr/` using the numeric prefix (e.g., `0005-brief-title.md`).
2. Fill the template in `adr/ADR_TEMPLATE.md` with Context, Decision, Consequences, Alternatives, and References.
3. Link the new ADR from `docs/adr_index.md`.
