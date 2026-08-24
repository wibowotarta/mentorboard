# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: MentorBoard
def _normalize(text):
    """Return normalized, non-empty text."""
    return (text or "").strip().replace("\n", " ").replace("  ", " ")


def _is_empty(value):
    """Return True if value is None, empty, or whitespace-only."""
    return not value or not _normalize(value)
