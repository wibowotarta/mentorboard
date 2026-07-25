# === Stage 50: Add unit tests for import and export behavior ===
# Project: MentorBoard
import unittest
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

class MockSessionTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, session_data):
        self.sessions.append(session_data)

    def export_to_json(self):
        return {"sessions": self.sessions}

    def load_from_json(self, json_str):
        import json
        data = json.loads(json_str)
        self.sessions = data["sessions"]

def test_import_export():
    tracker = MockSessionTracker()
    session_data = {
        "session_id": 1,
        "goals": ["Prepare Python project"],
        "questions": ["How to use Git?"]
    }
    tracker.add_session(session_data)

    json_str = tracker.export_to_json()
    assert isinstance(json_str, str)
    assert len(json_str) > 0

    loader = unittest.mock.patch("io.StringIO", new_callable=StringIO)
    with loader:
        import io
        captured = StringIO()
        with redirect_stdout(captured):
            pass

if __name__ == "__main__":
    test_import_export()
