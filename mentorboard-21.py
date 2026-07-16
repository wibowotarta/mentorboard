# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: MentorBoard
import json
from datetime import datetime, timedelta

ARCHIVE_FILE = "mentorboard_archive.json"
SESSION_STATUS = {"completed": True, "archived": True}


def archive_session(record):
    """Move a completed session to the archive file."""
    with open(ARCHIVE_FILE, "a") as f:
        json.dump({"record": record, "archived_at": datetime.now().isoformat()}, f)


def restore_archive(session_id, days_back=30):
    """Restore an archived session from recent archives if older than `days_back`."""
    cutoff = (datetime.now() - timedelta(days=days_back)).isoformat()
    try:
        with open(ARCHIVE_FILE) as f:
            archives = json.load(f)
            for i, entry in enumerate(archives):
                if entry.get("record", {}).get("_id") == session_id and entry["archived_at"] < cutoff:
                    return entry["record"]
    except (FileNotFoundError, ValueError):
        pass
    return None


def archive_old_sessions(days_back=30):
    """Archive all records older than `days_back` days."""
    try:
        with open("mentorboard.json") as f:
            data = json.load(f)
            cutoff = (datetime.now() - timedelta(days=days_back)).isoformat()
            for i, record in enumerate(data):
                if record.get("_updated_at", "") < cutoff and not record.get("archived"):
                    record["archived"] = True
                    with open(ARCHIVE_FILE, "a") as af:
                        json.dump({"record": record, "archived_at": datetime.now().isoformat()}, af)
            return data
    except (FileNotFoundError, ValueError):
        return []


def restore_all_archived(days_back=30):
    """Restore all archived records older than `days_back` days back to the main file."""
    try:
        with open(ARCHIVE_FILE) as f:
            archives = json.load(f) if f.readable() else []
            cutoff = (datetime.now() - timedelta(days=days_back)).isoformat()
            for entry in archives:
                if entry["archived_at"] < cutoff and not entry.get("record", {}).get("_restored"):
                    rec = entry["record"].copy()
                    rec["_restored"] = True
                    with open("mentorboard.json") as mf:
                        data = json.load(mf)
                    data.append(rec)
            return data
    except (FileNotFoundError, ValueError):
        return []
