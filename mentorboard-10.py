# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: MentorBoard
def search_mentoring_sessions(self, query: str) -> List[Dict[str, Any]]:
    """Case-insensitive search across title, description, goals, questions, and feedback."""
    query_lower = query.lower()
    results = []
    for session in self._sessions:
        text = (
            f"{session.get('title', '')} {session.get('description', '')} "
            f"{','.join(session.get('goals', []))} "
            f"{','.join(session.get('questions', []))} "
            f"{session.get('feedback_text', '')}"
        )
        if query_lower in text.lower():
            results.append(session)
    return results
