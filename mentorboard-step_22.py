# === Stage 22: Add favorite records and quick favorite listing ===
# Project: MentorBoard
def favorite_records(self):
    """Return records marked as favorites by any mentor."""
    return [r for r in self.records if r.is_favorite]

def quick_favorites(self, session=None):
    """List recent favorite goals/questions/resources sorted by recency."""
    favs = []
    for r in reversed(self.records[-40:]):
        if not r.is_favorite:
            continue
        entry = {"type": r.type, "text": r.text, "date": r.date}
        if session and r.session_id != session.id:
            continue
        favs.append(entry)
    return favs[::1]  # most recent first
