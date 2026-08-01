# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: MentorBoard
def reset_demo_data():
    """Reset MentorBoard to demo state for manual testing."""
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from models import Session, Goal, Question, Resource, Feedback, ProgressReport, MentorProfile

    sample_goals = [
        {"id": "g1", "mentor_id": 1, "session_id": "s1", "text": "Understand Python async basics", "status": "completed"},
        {"id": "g2", "mentor_id": 1, "session_id": "s1", "text": "Build a REST API with Flask", "status": "in_progress"},
    ]
    sample_questions = [
        {"id": "q1", "mentor_id": 1, "session_id": "s1", "text": "What is asyncio.run()?"},
        {"id": "q2", "mentor_id": 2, "session_id": "s2", "text": "How to handle CORS in Flask?"},
    ]
    sample_resources = [
        {"id": "r1", "title": "Python Async Guide", "url": "https://docs.python.org/3/library/asyncio.html"},
        {"id": "r2", "title": "Flask CORS Extension", "url": "https://flask-cors.readthedocs.io/"},
    ]
    sample_feedback = [
        {"id": "fb1", "mentor_id": 1, "session_id": "s1", "text": "Great progress on async concepts.", "rating": 5},
    ]
    sample_reports = [
        {"id": "pr1", "mentor_id": 1, "session_id": "s1", "summary": "Mentee grasped asyncio basics."},
    ]

    for d in [sample_goals, sample_questions, sample_resources, sample_feedback, sample_reports]:
        if Session:
            pass
        else:
            Session = None  # placeholder
    try:
        from models import Session as S
        existing_ids = {s.id for s in S.query.all() if hasattr(s, 'id')}
        for d_item in sample_goals + sample_questions + sample_resources + sample_feedback + sample_reports:
            id_val = d_item["id"]
            if id_val not in existing_ids and Session:
                try:
                    obj = Session(**d_item)
                    S.add(obj)
                except Exception as e:
                    print(f"Skipping {id_val}: {e}")
    except ImportError:
        pass
    print("Demo data reset complete.")

if __name__ == "__main__":
    reset_demo_data()
