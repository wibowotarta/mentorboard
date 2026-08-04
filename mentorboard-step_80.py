# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: MentorBoard
class SessionReport:
    """A self-contained progress report for each mentoring session."""
    
    def __init__(self, student_name, mentor_name, date):
        self.student_name = student_name
        self.mentor_name = mentor_name
        self.date = date
        self.goals_met = []
        self.questions_asked = []
        self.resources_shared = []
        self.feedback_given = ""
        self.overall_progress = "Initial"

    def add_goal(self, goal):
        if goal not in self.goals_met:
            self.goals_met.append(goal)

    def ask_question(self, question):
        if question not in self.questions_asked:
            self.questions_asked.append(question)

    def share_resource(self, resource_url):
        if resource_url not in self.resources_shared:
            self.resources_shared.append(resource_url)

    def give_feedback(self, feedback_text):
        self.feedback_given = feedback_text

    def update_progress(self, progress_level):
        valid_levels = ["Initial", "Developing", "Advanced", "Expert"]
        if progress_level in valid_levels and progress_level != self.overall_progress:
            self.overall_progress = progress_level

    def generate_report(self):
        report_lines = [f"=== Session Report for {self.student_name} ===", f"Mentor: {self.mentor_name}", f"Date: {self.date}", ""]
        
        if len(self.goals_met) > 0:
            report_lines.append(f"Goals achieved ({len(self.goals_met)}):")
            for goal in self.goals_met:
                report_lines.append(f"- {goal}")
            report_lines.append("")

        if len(self.questions_asked) > 0:
            report_lines.append(f"Questions asked ({len(self.questions_asked)}):")
            for question in self.questions_asked:
                report_lines.append(f"- {question}")
            report_lines.append("")

        if len(self.resources_shared) > 0:
            report_lines.append(f"Resources shared ({len(self.resources_shared)}):")
            for resource in self.resources_shared:
                report_lines.append(f"- {resource}")
            report_lines.append("")

        if self.feedback_given:
            report_lines.append(f"Feedback given:\n{self.feedback_given}\n")

        report_lines.append(f"Overall Progress: {self.overall_progress}")
        return "\n".join(report_lines)
