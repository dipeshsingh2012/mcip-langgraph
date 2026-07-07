from typing import Any, Dict
from graph.state import PatientCase


def collect_intake(case: PatientCase, intake_data: Dict[str, Any]) -> Dict[str, Any]:
    state = case.model_dump()
    state.update(intake_data)
    state.setdefault("audit_log", []).append("agents.intake: intake data merged")
    return state
