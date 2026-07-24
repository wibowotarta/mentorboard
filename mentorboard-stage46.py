# === Stage 46: Add a schema version field and migration helper ===
# Project: MentorBoard
SCHEMA_VERSION = 46

def migrate_to_v46(db):
    """Add a schema_version column and record current version."""
    db.execute("ALTER TABLE mentoring_sessions ADD COLUMN IF NOT EXISTS schema_version INTEGER DEFAULT ?;", (SCHEMA_VERSION,))
    db.commit()
