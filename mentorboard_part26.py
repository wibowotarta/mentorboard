# === Stage 26: Add weekly summary calculations ===
# Project: MentorBoard
def weekly_summary(records):
    """Aggregate mentoring records into a compact weekly report."""
    week = {}
    for r in records:
        if "date" not in r:
            continue
        d = r["date"][:10]  # YYYY-MM-DD
        key = (d[:7], d[5:7])  # (year, isoweek)
        w = week.setdefault(key, {"goals": [], "questions": [], "resources": [], "feedbacks": [], "sessions": 0})
        for k in ["goals", "questions", "resources", "feedbacks"]:
            if isinstance(r.get(k), list):
                w[k].extend(r[k])
        w["sessions"] += 1
    return week
