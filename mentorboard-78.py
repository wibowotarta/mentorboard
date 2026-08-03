# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: MentorBoard
import os, json
from pathlib import Path

def _load_json(path: str) -> dict:
    with open(path) as f: return json.load(f)

def _save_json(data: dict, path: str) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    os.replace(tmp, path)

def get_mentor_board_path() -> Path:
    base = Path(__file__).resolve().parent.parent or "."
    return (base / "mentorboard" / "data").absolute()

def list_sessions() -> dict[str, dict]:
    d = _load_json(get_mentor_board_path() / "sessions.json")
    return {k: {**v, "_id": k} for k, v in d.items()} if isinstance(d, dict) else {}

def get_session(session_id: str) -> dict | None:
    return list_sessions().get(session_id)

def create_session(data: dict) -> dict:
    sid = "session_" + "".join(os.urandom(4).hex())
    _save_json({sid: data}, get_mentor_board_path() / "sessions.json")
    return {**data, "_id": sid}

def update_goal(session_id: str, goal_text: str) -> dict | None:
    s = get_session(session_id)
    if not s or "goals" not in s:
        s["goals"] = []
    for g in s["goals"]:
        if g.get("text") == goal_text:
            return s
    s["goals"].append({"id": sid + "_g" + str(len(s.get("_ids", []))), "text": goal_text})
    return s

def list_goals(session_id: str) -> list[dict]:
    s = get_session(session_id) or {}
    return s.get("goals", [])

def add_question(session_id: str, question_text: str) -> dict | None:
    s = get_session(session_id)
    if not s or "questions" not in s:
        s["questions"] = []
    qid = sid + "_q" + "".join(os.urandom(2).hex())
    s["questions"].append({"id": qid, "text": question_text})
    return s

def list_questions(session_id: str) -> list[dict]:
    s = get_session(session_id) or {}
    return s.get("questions", [])

def add_resource(session_id: str, title: str, url: str) -> dict | None:
    s = get_session(session_id)
    if not s or "resources" not in s:
        s["resources"] = []
    rid = sid + "_r" + "".join(os.urandom(2).hex())
    s["resources"].append({"id": rid, "title": title, "url": url})
    return s

def list_resources(session_id: str) -> list[dict]:
    s = get_session(session_id) or {}
    return s.get("resources", [])

def add_feedback(session_id: str, text: str) -> dict | None:
    s = get_session(session_id)
    if not s or "feedback" not in s:
        s["feedback"] = []
    fid = sid + "_fb" + "".join(os.urandom(2).hex())
    s["feedback"].append({"id": fid, "text": text})
    return s

def list_feedback(session_id: str) -> list[dict]:
    s = get_session(session_id) or {}
    return s.get("feedback", [])

def generate_progress_report(session_id: str) -> dict | None:
    s = get_session(session_id) or {}
    goals = s.get("goals", [])
    questions = s.get("questions", [])
    resources = s.get("resources", [])
    feedback = s.get("feedback", [])
    return {"session": session_id, "goal_count": len(goals), "question_count": len(questions),
            "resource_count": len(resources), "feedback_count": len(feedback)}

def get_all_sessions() -> list[dict]:
    d = _load_json(get_mentor_board_path() / "sessions.json") or {}
    return [v for v in d.values()]
