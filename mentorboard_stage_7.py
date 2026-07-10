# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: MentorBoard
def format_session_summary(session):
    return (f"Session: {session['topic']}\n"
            f"Goals:  {', '.join(session.get('goals', [])) or 'None'}\n"
            f"Q&A:     {len(session.get('questions', []))} questions\n"
            f"Resources: {', '.join(session.get('resources', [])[:3])}" +
            (f", ... ({len(session['resources']) - 3}) more" if len(session.get('resources', [])) > 3 else "") + "\n")

def format_progress_report(report):
    return (f"Name: {report['name']}\n"
            f"Level: {report['level']}\n"
            f"Hours: {report['hours']:.1f}h\n"
            f"Sessions completed: {report.get('sessions_completed', 0)}\n"
            f"Weak areas: {'; '.join(report.get('weak_areas', [])) or 'None'}")
