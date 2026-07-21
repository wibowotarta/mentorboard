# === Stage 38: Add data integrity checks for broken references ===
# Project: MentorBoard
import re


def check_references(data: dict) -> list[str]:
    errors = []
    if "sessions" not in data and "resources" not in data:
        errors.append("Missing 'sessions' or 'resources' key")
        return errors
    for s in data.get("sessions", []) + data.get("resources", []):
        ref = s.get("_ref")
        if ref is None:
            continue
        target_type, _, target_id = ref.partition("|")
        if not re.fullmatch(r"[a-z_]+|[A-Z][a-zA-Z0-9_]++", target_type):
            errors.append(f"Invalid reference type in {ref}")
        elif target_id and not re.fullmatch(r"\d+", target_id):
            errors.append(f"Non-numeric target id in {ref}")
    return errors


def validate_session_integrity(session: dict) -> list[str]:
    issues = []
    missing = [k for k in ("id", "mentor", "mentee") if k not in session]
    if missing:
        issues.extend(f"Missing required field '{k}' in session" for k in missing)
    goals = [g for g in (session.get("goals") or []) if isinstance(g, dict)]
    resources = [r for r in (session.get("resources") or []) if isinstance(r, dict)]
    questions = [q for q in (session.get("questions") or []) if isinstance(q, dict)]
    feedbacks = session.get("feedback", [])
    for g in goals:
        if not all(k in g for k in ("goal", "status")):
            issues.append(f"Goal missing 'goal' or 'status': {g}")
    for r in resources:
        if not all(k in r for k in ("title", "url")):
            issues.append(f"Resource missing 'title' or 'url': {r}")
    for q in questions:
        if "question" not in q and "answer" not in q:
            issues.append(f"Question must have 'question' or 'answer': {q}")
    return issues


def run_integrity_checks(data: dict) -> tuple[list[str], bool]:
    ref_errors = check_references(data)
    session_issues = []
    for s in data.get("sessions", []):
        if isinstance(s, dict):
            session_issues.extend(validate_session_integrity(s))
    all_errors = ref_errors + session_issues
    return all_errors, len(all_errors) == 0
