# === Stage 40: Add plain text report export ===
# Project: MentorBoard
def export_session_text(self, filename="report.txt"):
    """Export a mentoring session to plain text."""
    lines = []
    lines.append(f"Session: {self.session_id}")
    lines.append(f"Date: {self.date}")
    if self.goal:
        lines.append(f"Goal: {self.goal}")
    if self.questions:
        for q in self.questions:
            lines.append(f"- Q: {q.question}")
            if q.answer:
                lines.append(f"  A: {q.answer}")
    if self.resources:
        for r in self.resources:
            lines.append(f"- R: {r.title} ({r.url})")
    if self.feedback:
        lines.append(f"Feedback: {self.feedback}")
    if self.progress:
        lines.append(f"Progress: {self.progress}")
    content = "\n".join(lines) + "\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename
