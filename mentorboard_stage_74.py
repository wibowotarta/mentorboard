# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: MentorBoard
def snapshot_diff(before: dict, after: dict) -> list[tuple[str, str]]:
    """Compare two state snapshots and return ordered (field, before_value, after_value) triples."""
    changes = []
    all_keys = set(before) | set(after)
    for key in sorted(all_keys):
        b_val = before.get(key) if isinstance(before, dict) else getattr(before, key, None)
        a_val = after.get(key) if isinstance(after, dict) else getattr(after, key, None)
        if b_val != a_val:
            changes.append((key, str(b_val), str(a_val)))
    return changes


def summarize_changes(changes: list[tuple[str, str]]) -> str:
    """Render a human-readable summary of the snapshot diff."""
    lines = ["Snapshot comparison:\n"]
    for field, old_v, new_v in changes:
        lines.append(f"  • {field}: {old_v} → {new_v}")
    return "\n".join(lines)
