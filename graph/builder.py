"""Graph builder skeleton for MCIP.

This file provides a minimal, editable skeleton for constructing a LangGraph
`StateGraph` for the MVP. It intentionally keeps implementation details
lightweight and defensive so you can iterate locally even if `langgraph` is
not yet installed.

Next steps:
- Replace placeholders with your real LangGraph node functions
- Implement node I/O, checkpointing, and persistence
- Wire LLM calls and retrievers in the Research/Documentation agents
"""
from typing import Optional

try:
    # langgraph API surface may differ depending on version; adapt as needed.
    from langgraph.graph import StateGraph
except Exception:  # pragma: no cover - graceful fallback when langgraph isn't installed
    StateGraph = None


def _intake_node(state: dict) -> dict:
    """Simple intake node: normalize incoming patient info.

    Replace with a LangGraph node/handler when wiring into the real graph.
    """
    # Example normalization (no side-effects)
    state.setdefault("symptoms", state.get("symptoms") or [])
    state.setdefault("medical_history", state.get("medical_history") or "")
    state.setdefault("audit_log", state.get("audit_log") or [])
    state["audit_log"].append("intake: normalized")
    return state


def _research_node(state: dict) -> dict:
    """Placeholder research node.

    Implement RAG retrieval + evidence aggregation here.
    """
    state.setdefault("research_results", ["placeholder: no retriever configured"]) 
    state["audit_log"].append("research: placeholder executed")
    return state


def _documentation_node(state: dict) -> dict:
    """Placeholder documentation node that drafts a note.

    Replace with LLM call to Gemini/Vertex AI and safety checks.
    """
    draft = state.get("draft_note") or "Draft note: (placeholder)"
    state["draft_note"] = draft
    state["audit_log"].append("documentation: drafted placeholder note")
    return state


def build_graph() -> Optional[object]:
    """Construct and return a LangGraph StateGraph-like object.

    Returns None if `langgraph` is not available — replace with a real
    `StateGraph` builder when you have the dependency installed.
    """
    if StateGraph is None:
        # No runtime available; return a lightweight callable object that
        # runs the placeholder pipeline for local testing.
        class LocalGraph:
            def run(self, state: dict) -> dict:
                state = _intake_node(state)
                state = _research_node(state)
                state = _documentation_node(state)
                return state

        return LocalGraph()

    # Example pattern using a hypothetical StateGraph API. Adjust to match
    # the version of langgraph you install.
    g = StateGraph(name="mcip_state_graph")

    # Pseudo-code: real API calls will differ — replace `add_node` with the
    # appropriate method (e.g., g.add_node or g.add_action).
    try:
        g.add_node("intake", func=_intake_node)
        g.add_node("research", func=_research_node)
        g.add_node("documentation", func=_documentation_node)
        # Add edges / routing as needed. Example (pseudo):
        # g.add_edge("intake", "research")
        # g.add_edge("research", "documentation")
    except Exception:
        # If the API differs, keep the graph object but log instructions
        # in the returned object to implement these bindings later.
        pass

    return g


def run_graph(graph: object, patient_state: dict) -> dict:
    """Execute the provided graph over `patient_state`.

    For the local graph returned when `langgraph` is absent, call `graph.run`.
    For a real `StateGraph`, adapt to its execution API (e.g., `graph.execute`).
    """
    if graph is None:
        raise RuntimeError("Graph is not initialized. Call build_graph() first.")

    # LocalGraph uses `run`; langgraph's StateGraph may use a different method.
    if hasattr(graph, "run"):
        return graph.run(patient_state)

    if hasattr(graph, "execute"):
        return graph.execute(patient_state)

    # Fallback: return input unchanged
    return patient_state
