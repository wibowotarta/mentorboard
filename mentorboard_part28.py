# === Stage 28: Add overdue item detection based on due dates ===
# Project: MentorBoard
from datetime import date, timedelta


def detect_overdue(items: list[dict]) -> dict[str, list[dict]]:
    """Return a dict mapping each overdue item to its days-overdue count."""
    today = date.today()
    overdue = {}
    for item in items:
        due_date_str = item.get("due_date") or item.get("target_date")
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
        except ValueError:
            continue
        days_left = (today - due_date).days
        if days_left < 0:
            overdue[item["id"]] = {"item": item, "days_overdue": -days_left}
    return overdue
