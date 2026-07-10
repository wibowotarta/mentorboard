# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: MentorBoard
def update(self, mentor_id: str, session_id: int, **changes) -> dict | None:
        """Update a mentor's record for a given session.

        Returns the updated record (or None if no matching row exists).
        All fields are optional; missing keys leave existing values untouched.
        Raises ValueError when updates touch an unknown record.
        """
        key = (mentor_id, session_id)
        try:
            row = self.data[key]
        except KeyError:
            raise ValueError(f"No mentor entry for id={mentor_id!r}, session_id={session_id}")

        allowed_fields = {
            "goals", "questions", "resources", "feedback", "progress", "status"
        }
        unknown = set(changes) - allowed_fields
        if unknown:
            raise ValueError(f"Unknown field(s): {unknown}")

        for field in changes:
            row[field] = changes[field]

        self.data[key] = row
        return dict(row)
