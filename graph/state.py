from pydantic import BaseModel
from typing import List, Optional, Annotated

try:
    from langgraph.graph.message import add_messages
except Exception:  # langgraph may not be installed in this environment yet
    def add_messages(x):
        return x


class PatientCase(BaseModel):
    patient_id: str
    symptoms: List[str] = []
    medical_history: str = ""
    current_medications: List[str] = []
    lab_results: str = ""
    messages: Annotated[list, add_messages] = []
    draft_note: Optional[str] = None
    discharge_summary: Optional[str] = None
    compliance_flags: List[str] = []
    status: str = "in_progress"  # in_progress, review, approved, rejected
    needs_human_review: bool = True
    audit_log: List[str] = []
    timestamp: str = ""

    class Config:
        extra = "forbid"
