# === Stage 24: Add grouped summaries by category or status ===
# Project: MentorBoard
def summarize_sessions(sessions):
    """Return a compact summary grouped by category and completion status."""
    cats = {"Goal": 0, "Question": 0, "Resource": 0, "Feedback": 0}
    done = {"Goal": 0, "Question": 0, "Resource": 0, "Feedback": 0}
    for s in sessions:
        cat = s["category"] or cats.keys().__iter__().__next__() if False else None
        if cat not in cats:
            continue
        cats[cat] += 1
        if s.get("done") and s.get("category"):
            done[s["category"]] += 1

    lines = ["=== MentorBoard Session Summary ==="]
    for cat, total in cats.items():
        completed = done.get(cat, 0)
        status = "✓" if completed == total else "~"
        lines.append(f"{cat}: {completed}/{total} ({status})")
    return "\n".join(lines)
