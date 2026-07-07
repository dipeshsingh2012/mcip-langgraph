from datetime import datetime, timezone
from typing import Any, Dict, List


def _append_audit(state: Dict[str, Any], event: str) -> None:
    state.setdefault("audit_log", []).append(event)


def intake_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state.setdefault("symptoms", state.get("symptoms") or [])
    state.setdefault("medical_history", state.get("medical_history") or "")
    state.setdefault("current_medications", state.get("current_medications") or [])
    state.setdefault("lab_results", state.get("lab_results") or "")
    state.setdefault("messages", state.get("messages") or [])
    _append_audit(state, "intake: normalized patient intake")
    return state


def research_node(state: Dict[str, Any]) -> Dict[str, Any]:
    symptoms = state.get("symptoms", [])
    history = state.get("medical_history", "")
    research_results: List[str] = []

    if symptoms:
        research_results.append(
            f"Reviewed evidence for symptoms: {', '.join(symptoms)}"
        )
    else:
        research_results.append("No symptoms were provided for research.")

    if history:
        research_results.append("Medical history reviewed for risk and comorbidity context.")

    if not symptoms and not history:
        research_results.append("No clinical context available for research.")

    state["research_results"] = research_results
    _append_audit(state, "research: placeholder evidence aggregation")
    return state


def documentation_node(state: Dict[str, Any]) -> Dict[str, Any]:
    symptoms = state.get("symptoms", [])
    medical_history = state.get("medical_history", "")
    draft = [
        "Patient Intake Summary:\n",
        f"- Patient ID: {state.get('patient_id', '<unknown>')}\n",
        f"- Symptoms: {', '.join(symptoms) if symptoms else 'None'}\n",
        f"- Medical History: {medical_history or 'None'}\n",
        "\nAssessment:\n",
        "- Review evidence and develop a preliminary plan.\n",
    ]
    state["draft_note"] = "".join(draft)
    state["messages"] = state.get("messages", [])
    _append_audit(state, "documentation: drafted placeholder note")
    return state


def compliance_node(state: Dict[str, Any]) -> Dict[str, Any]:
    flags: List[str] = []
    medications = state.get("current_medications", [])
    if not isinstance(medications, list):
        medications = [medications]

    if not state.get("medical_history"):
        flags.append("missing_medical_history")

    if any(str(med).lower() == "unapproved" for med in medications):
        flags.append("contains_unapproved_medication")

    state["compliance_flags"] = flags
    state["status"] = "review" if flags else "approved"
    state["needs_human_review"] = bool(flags)
    _append_audit(state, "compliance: placeholder evaluation")
    return state


def finalize_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state.setdefault("completed_at", datetime.now(timezone.utc).isoformat())
    _append_audit(state, "finalize: case completed")
    return state
