# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: MentorBoard
def tag_add(self, tag: str):
    if self.tags is None:
        self.tags = []
    if tag.lower() not in [t.lower() for t in self.tags]:
        self.tags.append(tag)

def tag_remove(self, tag: str):
    if self.tags is not None:
        normalized = {t.lower(): t for t in self.tags}
        if tag.lower() in normalized:
            del self.tags[normalized[tag.lower()].index(tag)]

def tagged_summary(self, tags=None):
    if tags is None and self.tags is None:
        return ""
    if tags is None:
        tags = list(self.tags) if self.tags else []
    lines = [f"Tags: {', '.join(tags)}"]
    for tag in tags:
        if tag.lower() in [t.lower() for t in self.tags]:
            lines.append(f"- Highlighted content related to '{tag}'.")
    return "\n".join(lines)
