# ADR 0004: RAG-First Approach with Strict Grounding

Date: 2026-07-07
Status: Accepted

Context
-------
LLMs can hallucinate; clinical domain requires evidence-grounded outputs and traceability of sources.

Decision
--------
Adopt a Retrieval-Augmented Generation (RAG) first approach: always ground agent responses with retrieved evidence and attach source citations.

Consequences
------------
- Pros: Reduces hallucinations, improves auditability, and increases clinician trust.
- Cons: Requires building and maintaining a retrieval index, and careful prompt engineering to ensure citations are used correctly.

Alternatives Considered
-----------------------
- No RAG (rejected: unacceptable risk for clinical outputs).
- Reactive RAG (only when uncertainty detected) — considered for future optimization.

References
----------
- HLD.md (Key Architecture Decisions)
