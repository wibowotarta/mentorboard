# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: MentorBoard
import json, uuid
from datetime import date

DB = {
    "sessions": [],
    "goals": {},
    "questions": {},
    "resources": {},
    "feedbacks": {},
}

def new_session(topic=""):
    return {"id": str(uuid.uuid4())[:8], "topic": topic, "date": date.today().isoformat()}

DB["sessions"].append(new_session("Python basics"))
