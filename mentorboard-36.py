# === Stage 36: Add templates for quickly creating common records ===
# Project: MentorBoard
def create_record(session_id, record_type, **kwargs):
    """Create a new mentoring record (Goal, Question, Resource, Feedback, or ProgressReport)"""
    if record_type == "Goal":
        return {"session_id": session_id, "type": "Goal", **kwargs}
    elif record_type == "Question":
        return {"session_id": session_id, "type": "Question", **kwargs}
    elif record_type == "Resource":
        return {"session_id": session_id, "type": "Resource", **kwargs}
    elif record_type == "Feedback":
        return {"session_id": session_id, "type": "Feedback", **kwargs}
    elif record_type == "ProgressReport":
        return {"session_id": session_id, "type": "ProgressReport", **kwargs}
    else:
        raise ValueError(f"Unknown record type: {record_type}")
