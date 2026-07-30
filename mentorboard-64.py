# === Stage 64: Add validation for relationship references ===
# Project: MentorBoard
def validate_references(data):
    """Cross-check that relationship references point to valid mentors/mentees."""
    errors = []
    for record in data:
        if "mentor" in record and record["mentor"] is not None:
            mentor_id = str(record["mentor"]).strip()
            if mentor_id not in [str(r.get("id")) for r in data if "id" in r]:
                errors.append(f"Mentor reference '{mentor_id}' not found.")

        if "mentee" in record and record["mentee"] is not None:
            mentee_id = str(record["mentee"]).strip()
            if mentee_id not in [str(r.get("id")) for r in data if "id" in r]:
                errors.append(f"Mentee reference '{mentee_id}' not found.")

        if "goals" in record and isinstance(record["goals"], list):
            goals = record["goals"]
            if len(goals) != 0:
                for goal in goals:
                    if "status" in goal and goal.get("target_date") is None:
                        errors.append(f"Goal '{goal.get('name', 'unknown')}' has no target_date.")

        if "feedback" in record and isinstance(record["feedback"], list):
            feedbacks = record["feedback"]
            for fb in feedbacks:
                if "timestamp" not in fb or not fb.get("timestamp"):
                    errors.append(f"Feedback entry missing timestamp.")

    return errors
