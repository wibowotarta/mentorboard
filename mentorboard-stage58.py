# === Stage 58: Add bulk update behavior for selected records ===
# Project: MentorBoard
def bulk_update_records(self, updates):
    """Update multiple records at once with a dict mapping record_id to {field: value}."""
    if not isinstance(updates, dict) or not all(
        isinstance(k, (int, str)) and isinstance(v, dict) for k, v in updates.items()
    ):
        raise ValueError("bulk_update_records expects {record_id: {field: new_value}}")

    with self._lock:
        count = 0
        for rid, fields in updates.items():
            if rid not in self._records:
                print(f"Warning: skipping unknown record id={rid}")
                continue
            for field, value in fields.items():
                if field == "id":
                    raise ValueError("Cannot update 'id' field")
                if field not in self.schema:
                    raise KeyError(f"Unknown field '{field}'")
                setattr(self._records[rid], field, value)
            count += 1

        print(
            f"[MentorBoard] bulk_update_records: {count}/{len(updates)} records updated."
        )
        return count
