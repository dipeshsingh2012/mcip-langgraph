from graph.nodes import intake_node


def test_intake_node_normalizes_input_and_sets_summary():
    state = {
        "patient_id": "patient-001",
        "symptoms": "fever, cough",
        "medical_history": "Asthma",
        "current_medications": "albuterol",
        "lab_results": "CBC pending",
    }

    result = intake_node(state)

    assert result["patient_id"] == "patient-001"
    assert result["symptoms"] == ["fever", "cough"]
    assert result["medical_history"] == "Asthma"
    assert result["current_medications"] == ["albuterol"]
    assert result["status"] == "in_progress"
    assert result["needs_human_review"] is False
    assert result["intake_summary"].startswith("Intake summary")
    assert any(event.startswith("intake:") for event in result["audit_log"])
