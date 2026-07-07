from typing import Any, Dict
from graph.state import PatientCase


def normalize_intake_payload(intake_data: Dict[str, Any]) -> Dict[str, Any]:
    # Create a copy so the original payload is not mutated in place.
    normalized = dict(intake_data or {})

    # Normalize symptoms from either a list or a comma-separated string.
    symptoms = normalized.get("symptoms", [])
    if isinstance(symptoms, str):
        symptoms = [item.strip() for item in symptoms.split(",") if item.strip()]
    elif symptoms is None:
        symptoms = []
    normalized["symptoms"] = symptoms

    # Normalize medications from either a list or a comma-separated string.
    medications = normalized.get("current_medications", [])
    if isinstance(medications, str):
        medications = [item.strip() for item in medications.split(",") if item.strip()]
    elif medications is None:
        medications = []
    normalized["current_medications"] = medications

    normalized["medical_history"] = normalized.get("medical_history") or ""
    normalized["lab_results"] = normalized.get("lab_results") or ""
    return normalized


def build_intake_summary(state: Dict[str, Any]) -> str:
    # Create a compact human-readable summary for the intake state.
    patient_id = state.get("patient_id", "unknown")
    symptoms = ", ".join(state.get("symptoms", []) or ["none"])
    history = state.get("medical_history") or "none"
    medications = ", ".join(state.get("current_medications", []) or ["none"])
    return (
        f"Intake summary for {patient_id}: "
        f"symptoms={symptoms}; medical_history={history}; "
        f"current_medications={medications}"
    )


def collect_intake(case: PatientCase, intake_data: Dict[str, Any]) -> Dict[str, Any]:
    # Merge the incoming intake payload into a plain dictionary state.
    state = case.model_dump()
    merged = normalize_intake_payload(intake_data)
    state.update(merged)
    state.setdefault("audit_log", []).append("agents.intake: intake data merged")
    return state
