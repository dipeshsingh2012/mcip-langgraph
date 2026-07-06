"""Minimal runner for MCIP skeleton.

Run this after creating and activating your virtualenv and installing dependencies:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
"""

from datetime import datetime
from graph.state import PatientCase
import json


def create_sample_case():
    pc = PatientCase(
        patient_id="sample-001",
        symptoms=["fever", "cough"],
        medical_history="No chronic illnesses.",
        current_medications=[],
        lab_results="CBC normal",
        timestamp=datetime.utcnow().isoformat() + "Z",
    )
    pc.audit_log.append("Created sample case")
    return pc


if __name__ == "__main__":
    case = create_sample_case()
    print("Sample PatientCase JSON:\n")
    print(json.dumps(case.dict(), indent=2))
    print("\nNext: implement `graph/builder.py` and LangGraph nodes to run flows.")
