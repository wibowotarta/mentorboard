# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: MentorBoard
class ValidationReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def check_session_date(self, session):
        if not session.get('date'):
            self.warnings.append("Session has no date")
        else:
            try:
                from datetime import datetime
                datetime.strptime(session['date'], '%Y-%m-%d')
            except ValueError:
                self.errors.append(f"Invalid date format in session '{session.get('id')}': {session['date']}")

    def check_goal_count(self, mentor_profile):
        goals = mentor_profile.get('goals', [])
        if not isinstance(goals, list) or len(goals) == 0:
            self.warnings.append(f"Mentor profile '{mentor_profile.get('id')}' has no goals")

    def check_feedback_presence(self, session):
        if 'feedback' in session and not session['feedback'].get('summary'):
            self.errors.append("Session feedback is missing a summary")

    def generate_report(self, mentor_profiles, sessions):
        for profile in mentor_profiles:
            self.check_goal_count(profile)
        for session in sessions:
            self.check_session_date(session)
            self.check_feedback_presence(session)
        if not self.warnings and not self.errors:
            return "All checks passed."
        report = f"Validation Report:\nErrors: {len(self.errors)}\nWarnings: {len(self.warnings)}\n\n"
        for err in self.errors:
            report += f"- Error: {err}\n"
        for warn in self.warnings:
            report += f"- Warning: {warn}\n"
        return report.strip()
