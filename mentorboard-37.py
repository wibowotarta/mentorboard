# === Stage 37: Add recommendations for the next useful action ===
# Project: MentorBoard
def recommend_next_action(session: Session, progress: ProgressReport) -> List[str]:
    """Generate actionable recommendations based on session context."""
    recs = []
    if not progress.goals_met and session.status == "in_progress":
        unmet = [g for g in progress.goals if not g.completed]
        if unmet:
            recs.append(f"Focus on completing: {', '.join(g.description[:40]) for g in unmet}")
    elif progress.next_review_date and (datetime.now() >= progress.next_review_date):
        recs.append("Schedule a follow-up session to review next milestones")
    if session.resources and any(r.type == "article" for r in session.resources):
        unread = [r for r in session.resources if not r.read]
        if unread:
            recs.append(f"Read assigned articles: {', '.join(r.title[:30] for r in unread)}")
    if progress.feedback and not progress.feedback.completed:
        recs.append("Complete the feedback form to finalize this mentoring cycle")
    if session.questions and any(q.unanswered for q in session.questions):
        recs.append("Answer remaining questions before closing the session")
    return recs if recs else ["Continue with current learning activities"]
