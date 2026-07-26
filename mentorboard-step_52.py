# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: MentorBoard
def format_session_summary(session):
    """Return a human-readable one-line summary of a mentoring session."""
    return (
        f"[{session['date']}] "
        f"Goal: {session.get('goal', 'none')} | "
        f"Qs: {len(session.get('questions', []))} | "
        f"Resources: {len(session.get('resources', []))}"
    )


def format_goal_report(goals):
    """Format a list of goals into a readable report string."""
    if not goals:
        return "No goals recorded."
    lines = ["Goal Report:", "", ""]
    for g in goals:
        status_marker = "[DONE]" if g.get("completed") else "[ACTIVE]"
        lines.append(f"  - {status_marker} {g['topic']} ({g['description']})")
    return "\n".join(lines)


def format_progress_report(records):
    """Summarize mentoring progress records into a compact report."""
    if not records:
        return "No progress records yet."
    total = len(records)
    completed = sum(1 for r in records if r.get("completed"))
    latest = max(r["date"] for r in records)
    avg_hours = (sum(r.get("hours", 0) for r in records) / total) if records else 0
    lines = [
        "Progress Report:", "",
        f"  Total sessions: {total}",
        f"  Completed: {completed}/{total}",
        f"  Latest session date: {latest}",
        f"  Avg hours/session: {avg_hours:.1f}h",
    ]
    return "\n".join(lines)
