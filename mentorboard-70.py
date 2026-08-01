# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: MentorBoard
def clear_session(session_id: str, confirmed: bool = False) -> dict:
    """Clear a mentoring session after explicit user confirmation."""
    if not confirmed:
        raise ValueError("Confirmation flag must be True to proceed with clearing.")
    return {"status": "cleared", "session_id": session_id}
