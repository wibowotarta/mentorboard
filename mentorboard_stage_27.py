# === Stage 27: Add monthly summary calculations ===
# Project: MentorBoard
import statistics
from collections import defaultdict


def monthly_summary(records):
    """Compute per-user monthly stats from mentoring session records."""
    user_monthly = defaultdict(lambda: defaultdict(list))
    for r in records:
        key = (r["user"], r.get("month", ""))
        user_monthly[r["user"]][key].append(r)

    summary = {}
    for user, months in user_monthly.items():
        stats = {"sessions": 0, "goals_met": [], "avg_session_minutes": None}
        total_min = 0
        count = 0
        for month, recs in months.items():
            if not month:
                continue
            stats["sessions"] += len(recs)
            for s in recs:
                goals_met = sum(1 for g in s.get("goals", []) if g.get("status") == "completed")
                stats["goals_met"].append(goals_met)
                total_min += s.get("duration_minutes", 0)
                count += 1
        avg = statistics.mean(stats["goals_met"]) if stats["goals_met"] else 0
        summary[user] = {
            "sessions": stats["sessions"],
            "avg_goals_per_session": round(avg, 2),
            "total_minutes": total_min,
            "avg_duration_minutes": (total_min / count) if count else None,
        }

    return dict(sorted(summary.items()))
