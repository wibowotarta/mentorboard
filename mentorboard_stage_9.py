# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: MentorBoard
def sort_sessions(sessions, key):
    order = {"title": 1, "date": 2, "priority": 3, "last_update": 4}
    if key not in order: raise ValueError(f"Unknown sort key: {key}")
    reverse_keys = {"date", "priority", "last_update"}
    return sorted(sessions, key=lambda s: (s.get(key) or "",), reverse=key in reverse_keys)
