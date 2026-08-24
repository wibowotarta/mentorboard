# === Stage 83: Add regression tests for the final demo workflow ===
# Project: MentorBoard
import pytest

def test_mentor_session_demonstration():
    session_id = "20240601"
    mentor = MentorProfile("Dr. Smith", "AI Research", "MIT")
    mentee = MentorProfile("Alex Chen", "ML Engineering", "Stanford")
    session = MentorSession(session_id, mentor, mentee)
    session.add_goal("Understand transformer attention mechanisms")
    session.add_question("How does self-attention work in BERT?")
    resource = Resource("Attention Is All You Need", "https://arxiv.org/abs/1706.03762")
    session.add_resource(resource)
    feedback = Feedback(
        mentor_comments="Alex grasped the concept quickly.",
        mentee_comments="Need more practice with positional encodings.",
        session_rating=4.5
    )
    session.add_feedback(feedback)
    progress = ProgressReport(
        session_id=session_id,
        topic="Attention in transformers",
        key_points=["Self-attention mechanism", "Positional encoding"],
        next_steps=["Implement masked attention", "Explore multi-head attention"],
        session_summary="Positive session with good engagement on core concepts."
    )
    session.add_progress_report(progress)
    assert session.get_full_report() == "Goal: Understand transformer attention mechanisms\nQuestion: How does self-attention work in BERT?\nResource: Attention Is All You Need (https://arxiv.org/abs/1706.03762)\nFeedback: Mentor: Alex grasped the concept quickly.\nMentee: Need more practice with positional encodings.\nRating: 4.5/5.0\nProgress: Topic: Attention in transformers\nKey points: Self-attention mechanism, Positional encoding\nNext steps: Implement masked attention, Explore multi-head attention\nSummary: Positive session with good engagement on core concepts."
