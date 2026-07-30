# === Stage 66: Add export of a short status dashboard ===
# Project: MentorBoard
def print_status_dashboard(mentor, mentee, sessions):
    """Print a compact status dashboard for a mentoring pair."""
    total = len(sessions)
    avg_score = sum(s.get("goal_score", 0) for s in sessions) / max(total, 1)
    print(f"=== MentorBoard Status Dashboard ===")
    print(f"Mentor: {mentor}")
    print(f"Mentee: {mentee}")
    print(f"Sessions held: {total}")
    print(f"Avg goal score: {avg_score:.1f}/5.0")
    if sessions:
        last = sessions[-1]
        print(f"Latest session date: {last.get('date', 'N/A')}")
        print(f"Last question answered: {last.get('question', 'N/A')}")
        print(f"Resources shared: {len(last.get('resources', []))}")
    print("=== End ===")
