# ADR 0002: Primary LLM = Gemini via Vertex AI

Date: 2026-07-07
Status: Accepted

Context
-------
The platform needs a production-capable LLM provider with strong performance, multimodal capabilities, and tight integration with GCP for compliance and observability.

Decision
--------
Use Google Vertex AI (Gemini models) as the primary LLM provider for MCIP.

Consequences
------------
- Pros: Native GCP integration, enterprise-grade features, multimodal support, and operational tooling (Vertex AI + LangGraph can be integrated cleanly).
- Cons: Platform lock-in to GCP for model serving; will need to document portability considerations.

Alternatives Considered
-----------------------
- Use a multi-cloud LLM provider (rejected for MVP due to increased integration effort).
- Self-host open-source models (rejected for MVP: resource and compliance constraints).

References
----------
- HLD.md (Key Architecture Decisions)
