# === Stage 45: Add restore from backup with validation ===
# Project: MentorBoard
def restore_from_backup(backup_path):
    """Restore a MentorBoard database from a backup JSON file with validation."""
    import json, os
    if not os.path.isfile(backup_path) or not backup_path.endswith('.json'):
        raise FileNotFoundError("Backup file is missing or invalid.")
    with open(backup_path) as f:
        data = json.load(f)
    expected_keys = {'sessions', 'goals', 'questions', 'resources', 'feedback', 'progress_reports'}
    if not expected_keys.issubset(data.keys()):
        raise ValueError("Backup file is missing required keys.")
    for table in data.values():
        if isinstance(table, list) and len(table) > 0:
            if not isinstance(table[0], dict):
                raise TypeError("Each backup entry must be a JSON object.")
    return data
