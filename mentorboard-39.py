# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: MentorBoard
def repair_data_integrity(records):
    """Repair common data integrity issues in mentoring session records."""
    repaired_count = 0
    for record in records:
        if isinstance(record, dict) and 'session_id' in record:
            try:
                record['session_id'] = str(record['session_id']).strip()
            except Exception:
                pass

            if not record.get('goals'):
                record['goals'] = []
            if not record.get('questions'):
                record['questions'] = []
            if not record.get('resources'):
                record['resources'] = []
            if not record.get('feedback'):
                record['feedback'] = {}

            for i, goal in enumerate(record.get('goals', [])):
                if isinstance(goal, str) and len(goal.strip()) == 0:
                    record['goals'].pop(i)
                    repaired_count += 1

        elif isinstance(record, dict) and 'student' in record:
            try:
                record['student'] = str(record['student']).strip()
            except Exception:
                pass

    return records
