# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: MentorBoard
def filter_sessions(sessions, status=None, category=None, owner=None, tag=None):
    """Filter mentoring sessions by optional criteria: status, category, owner, tag."""
    results = []
    for s in sessions:
        if status is not None and s.get("status") != status:
            continue
        if category is not None and s.get("category") != category:
            continue
        if owner is not None and s.get("owner") != owner:
            continue
        if tag is not None:
            tags = s.get("tags", [])
            if tag not in tags:
                continue
        results.append(s)
    return results
