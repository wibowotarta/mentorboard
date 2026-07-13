# === Stage 11: Add JSON export for the current application state ===
# Project: MentorBoard
import json


def export_state(app):
    state = {
        "sessions": app.sessions,
        "user_goals": app.user_goals,
        "resources": app.resources,
        "settings": app.settings,
    }
    return json.dumps(state, indent=2)


if __name__ == "__main__":
    # Example usage with a simple in-memory state
    sample_state = {
        "sessions": [{"id": 1, "topic": "Python basics", "status": "completed"}],
        "user_goals": ["Learn Python", "Build MentorBoard"],
        "resources": [{"title": "Python Crash Course", "url": "https://example.com"}],
        "settings": {"theme": "dark", "language": "en"},
    }
    exported = export_state(sample_state)
    print(exported[:200] + "...")  # Print first 200 chars
