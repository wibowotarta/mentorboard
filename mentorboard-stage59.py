# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: MentorBoard
def bulk_delete(self, ids: list[str], *, confirmed: bool) -> int:
        """Delete mentor sessions in batches; confirm before execution."""
        if not confirmed:
            raise RuntimeError(
                "Bulk delete requires explicit user confirmation."
            )
        deleted = 0
        for batch_ids in self._chunks(ids):
            with self.lock:
                count = 0
                for s in list(self.sessions.values()):
                    if s["id"] in batch_ids:
                        self.sessions.pop(s["id"], None)
                        count += 1
                deleted += count
        return deleted
