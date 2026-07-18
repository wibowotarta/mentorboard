# === Stage 25: Add daily summary calculations ===
# Project: MentorBoard
def daily_summary(sessions):
    """Compute a compact daily summary from a list of session dicts."""
    today = max((s.get("date", "") for s in sessions), default="")
    if not today:
        return {"date": "", "total_sessions": 0, "avg_duration_min": 0}

    total = sum(1 for s in sessions if s.get("date") == today)
    durations = [float(s.get("duration_min", 0)) for s in sessions if s.get("date") == today]
    avg_dur = round(sum(durations) / len(durations), 1) if durations else 0

    return {
        "date": today,
        "total_sessions": total,
        "avg_duration_min": avg_dur,
    }
