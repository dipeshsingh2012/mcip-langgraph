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
from typing import Optional, TypedDict

try:
    # langgraph API surface may differ depending on version; adapt as needed.
    from langgraph.graph import StateGraph
except Exception:  # pragma: no cover - graceful fallback when langgraph isn't installed
    StateGraph = None

from graph.nodes import (
    compliance_node,
    documentation_node,
    finalize_node,
    intake_node,
    research_node,
)


def build_graph() -> Optional[object]:
    """Construct and return a LangGraph StateGraph-like object.

    Returns None if `langgraph` is not available — replace with a real
    `StateGraph` builder when you have the dependency installed.
    """
    if StateGraph is None:
        class LocalGraph:
            def run(self, state: dict) -> dict:
                state = intake_node(state)
                state = research_node(state)
                state = documentation_node(state)
                state = compliance_node(state)
                state = finalize_node(state)
                return state

        return LocalGraph()

    try:
        g = StateGraph()
    except TypeError:
        # Some langgraph versions require a `state_schema` TypedDict at init.
        # Provide a minimal, permissive schema so the builder can be created.
        try:
            StateSchema = TypedDict(
                "StateSchema",
                {
                    "patient_id": str,
                    "symptoms": list,
                    "medical_history": str,
                    "current_medications": list,
                    "lab_results": str,
                    "messages": list,
                    "draft_note": str,
                    "discharge_summary": str,
                    "compliance_flags": list,
                    "status": str,
                    "needs_human_review": bool,
                    "audit_log": list,
                    "timestamp": str,
                },
                total=False,
            )
            g = StateGraph(state_schema=StateSchema)
        except Exception:
            # If instantiation still fails, re-raise the original TypeError
            raise

    # Prefer the `add_sequence` API for ordered node registration (langgraph v1.2+).
    try:
        g.add_sequence([
            intake_node,
            research_node,
            documentation_node,
            compliance_node,
            finalize_node,
        ])
        # Set entry/finish points using inferred callable names.
        try:
            g.set_entry_point("intake_node")
            g.set_finish_point("finalize_node")
        except Exception:
            pass
    except Exception:
        # Fall back to older per-node registration if available.
        try:
            g.add_node("intake", func=intake_node)
            g.add_node("research", func=research_node)
            g.add_node("documentation", func=documentation_node)
            g.add_node("compliance", func=compliance_node)
            g.add_node("finalize", func=finalize_node)
            try:
                g.set_entry_point("intake")
                g.set_finish_point("finalize")
            except Exception:
                pass
        except Exception:
            pass

    return g


def run_graph(graph: object, patient_state: dict) -> dict:
    """Execute the provided graph over `patient_state`.

    For local testing the lightweight `LocalGraph.run` is used.
    For real `StateGraph` instances, compile with `StateGraph.compile()` and
    invoke the resulting runnable via `invoke()` / `stream()` / `ainvoke()`.
    """
    if graph is None:
        raise RuntimeError("Graph is not initialized. Call build_graph() first.")

    # If the object already implements the Runnable/compiled API, prefer it.
    if hasattr(graph, "invoke"):
        return graph.invoke(patient_state)

    # Backwards-compatible local fallback for the lightweight LocalGraph.
    if hasattr(graph, "run"):
        return graph.run(patient_state)

    if hasattr(graph, "execute"):
        return graph.execute(patient_state)

    # If we were given a StateGraph builder, compile it to a runnable and invoke.
    try:
        from langgraph.graph import StateGraph
    except Exception:
        StateGraph = None

    if StateGraph is not None and isinstance(graph, StateGraph):
        compiled = graph.compile()
        if hasattr(compiled, "invoke"):
            return compiled.invoke(patient_state)

    # Fallback: return the input state unchanged
    return patient_state
