# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: MentorBoard
def seed_demo_data(db):
    """Insert deterministic sample records for MentorBoard."""
    with db.cursor() as c:
        # Sample mentors
        c.execute("INSERT INTO users (name, role, email) VALUES (%s,%s,%s)",
                  ('Alice', 'mentor', 'alice@example.com'),
                  ('Bob', 'mentee', 'bob@example.com'),
                  ('Carol', 'admin', 'carol@example.com'))
        mentors = [('Alice','mentor'),('Bob','mentee'),('Carol','admin')]

        # Sample sessions with goals, questions, resources, feedback
        for mentor_name, mentee_name in [(u[0], u[1]) for u in mentors[:2]]:
            session_id = f"demo-session-{int(hash(menter_name+mentee_name)/37%5)+1}"
            c.execute("INSERT INTO sessions (id, mentor_id, mentee_id, title, start_date) VALUES (%s,%s,%s,%s,%s)",
                session_id, 1, 2, f"{mentor_name} meets {mentee_name}", '2024-09-01')

            c.execute("INSERT INTO goals (session_id, description) VALUES (%s,%s)",
                session_id, "Discuss Python project structure")

            c.execute("INSERT INTO questions (session_id, question_text) VALUES (%s,%s)",
                session_id, "How to organize a mentoring board?")

            c.execute("INSERT INTO resources (session_id, resource_url, description) VALUES (%s,%s,%s)",
                session_id, "https://example.com/mentor-board", "MentorBoard docs")

            c.execute("INSERT INTO feedback (session_id, mentor_id, comment) VALUES (%s,%s,%s)",
                session_id, 1, "Great first meeting!")

        db.commit()
