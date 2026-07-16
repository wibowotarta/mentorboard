# === Stage 20: Add duplicate detection for newly created records ===
# Project: MentorBoard
def check_duplicate(record, db_path):
    """Return True if a record with matching key fields already exists in the DB."""
    try:
        with open(db_path, "r") as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    keys = list(record.keys())
    for ex in existing:
        if all(ex.get(k) == record.get(k) for k in keys):
            return True
    return False
