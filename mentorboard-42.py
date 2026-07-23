# === Stage 42: Add CSV export without external dependencies ===
# Project: MentorBoard
def export_to_csv(mentors, filename="mentorboard.csv"):
    """Export all Mentor objects to a CSV file without external dependencies."""
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Status", "Sessions Completed"])
        for mentor in mentors:
            writer.writerow([
                getattr(mentor, "name", ""),
                getattr(mentor, "email", ""),
                getattr(mentor, "status", ""),
                getattr(mentor, "_sessions_completed", 0),
            ])
    print(f"Exported {len(mentors)} mentors to {filename}")
