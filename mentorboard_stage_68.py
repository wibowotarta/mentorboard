# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: MentorBoard
def generate_changelog():
    """Generate a compact changelog from tracked activity."""
    entries = []
    for session in sessions:
        if session.get('goals'):
            goals_str = ', '.join(session['goals'])
            entries.append(f"[{session['date']}]: Goals set - {goals_str}")
        if session.get('questions'):
            questions_str = '; '.join(session['questions'][:3])
            entries.append(f"[{session['date']}]: Questions raised - {questions_str}")
        if session.get('resources'):
            resources_str = ', '.join(session['resources'][:5])
            entries.append(f"[{session['date']}]: Resources shared - {resources_str}")
        if session.get('feedback'):
            feedback = session['feedback'].get('summary', '')
            entries.append(f"[{session['date']}]: Feedback received - {feedback}")
        if session.get('progress_report'):
            report = session['progress_report'].get('status', '')
            entries.append(f"[{session['date']}]: Progress update - {report}")
    return '\n'.join(entries)
