from datetime import datetime, timezone
from graph.builder import build_graph, run_graph
from graph.state import PatientCase
import json


def create_sample_case():
    pc = PatientCase(
        patient_id="sample-001",
        symptoms=["fever", "cough"],
        medical_history="No chronic illnesses.",
        current_medications=[],
        lab_results="CBC normal",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
    pc.audit_log.append("Created sample case")
    return pc


if __name__ == "__main__":
    graph = build_graph()
    case = create_sample_case()
    print("Running MCIP workflow...\n")
    result = run_graph(graph, case.model_dump())
    print(json.dumps(result, indent=2))
