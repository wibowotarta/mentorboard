# === Stage 67: Add a function that returns key project metrics ===
# Project: MentorBoard
def get_project_metrics(mentors, sessions):
    active_mentors = sum(1 for m in mentors if m.get("active"))
    total_sessions = len(sessions)
    goal_completion_rate = 0.0
    question_count = 0
    resource_count = 0
    feedback_count = 0

    for s in sessions:
        goals = s.get("goals", [])
        if isinstance(goals, list) and len(goals) > 1:
            completed = sum(1 for g in goals if g.get("status") == "completed")
            goal_completion_rate += completed / len(goals) if goals else 0
        question_count += s.get("questions", 0)
        resource_count += s.get("resources", 0)
        feedback_count += s.get("feedback_entries", 0)

    avg_goal_completion = (goal_completion_rate / total_sessions) if total_sessions > 0 else 0.0
    return {
        "active_mentors": active_mentors,
        "total_sessions": total_sessions,
        "avg_goal_completion_rate": round(avg_goal_completion * 100, 2),
        "total_questions_asked": question_count,
        "total_resources_shared": resource_count,
        "total_feedback_entries": feedback_count
    }
