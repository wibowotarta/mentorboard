# === Stage 4: Implement create operations for the primary records ===
# Project: MentorBoard
def create_session(self, mentor_id, mentee_id, topic, scheduled_at):
    session = Session(mentor_id=mentor_id, mentee_id=mentee_id, topic=topic, scheduled_at=scheduled_at)
    self.sessions.append(session)
    return session

def create_goal(self, mentee_id, title, description, target_date):
    goal = Goal(mentee_id=mentee_id, title=title, description=description, target_date=target_date)
    self.goals.append(goal)
    return goal

def create_question(self, mentee_id, session_id, question_text):
    if not self.sessions:
        raise ValueError("No sessions exist to link questions to")
    session = self.sessions[0]
    q = Question(session=session, text=question_text)
    self.questions.append(q)
    return q

def create_resource(self, mentee_id, title, url):
    resource = Resource(mentee_id=mentee_id, title=title, url=url)
    self.resources.append(resource)
    return resource

def create_feedback(self, session_id, feedback_text, rating=None):
    if not self.sessions:
        raise ValueError("No sessions exist to link feedback to")
    session = self.sessions[0]
    fb = Feedback(session=session, text=feedback_text, rating=rating)
    self.feedbacks.append(fb)
    return fb

def create_progress_report(self, mentee_id, period_start, period_end):
    report = ProgressReport(mentee_id=mentee_id, period_start=period_start, period_end=period_end)
    self.reports.append(report)
    return report
