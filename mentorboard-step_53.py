# === Stage 53: Add command help text and usage examples ===
# Project: MentorBoard
def print_help():
    """Print MentorBoard usage help and examples."""
    print("MentorBoard - Mentoring Session Tracker\n")
    print("Usage:")
    print("  mentorboard --add-session <goals> <questions> [resources]")
    print("  mentorboard --feedback <session_id> <rating> [comment]")
    print("  mentorboard --progress <session_id>")
    print()
    print("Examples:")
    print('  mentorboard --add-session "Learn Git" "What is CI/CD?"')
    print("  mentorboard --feedback s1 5 \"Great session!\"")
    print("  mentorboard --progress s1")
