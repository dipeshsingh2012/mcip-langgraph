from typing import Any, Dict


def compliance_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    state.setdefault("compliance_flags", [])
    if not state.get("medical_history"):
        state["compliance_flags"].append("missing_medical_history")
    if state.get("status") == "approved":
        state.setdefault("audit_log", []).append("agents.compliance: verified approved state")
    else:
        state.setdefault("audit_log", []).append("agents.compliance: placeholder compliance review")
    return state
