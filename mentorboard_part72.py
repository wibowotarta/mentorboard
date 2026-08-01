# === Stage 72: Add Markdown report export ===
# Project: MentorBoard
def export_markdown_report(report):
    """Export a MentorBoard report to markdown format."""
    md = f"# Mentoring Session Report\n\n"
    md += f"**Attendees:** {report.get('attendees', [])}\n\n"
    md += f"**Goals Covered:**\n"
    for goal in report.get("goals_covered", []):
        md += f"- [{goal.get('status', 'pending')}] {goal.get('description', '')}\n"
    md += "\n**Questions Discussed:**\n"
    for q in report.get("questions_discussed", []):
        md += f"- **{q.get('topic', '')}**: {q.get('summary', '')}\n"
    md += "\n**Resources Shared:**\n"
    for r in report.get("resources_shared", []):
        md += f"- [{r.get('type', 'link')}] {r.get('title', '')}: {r.get('url', '')}\n"
    if report.get("feedback"):
        md += "\n**Feedback:**\n"
        for entry in report["feedback"]:
            md += f"- **{entry.get('from_role', 'Mentor')}**: {entry.get('content', '')}\n"
    return md
