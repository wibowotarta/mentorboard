# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: MentorBoard
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MentorGoal:
    goal_id: str = ""
    title: str = ""
    description: str = ""
    is_complete: bool = False

    def __post_init__(self):
        if not self.goal_id:
            self.goal_id = f"goal_{len(self.__class__.__dict__.get('_goals', [])) + 1}"


@dataclass
class MentorQuestion:
    question_id: str = ""
    text: str = ""
    category: str = "general"

    def __post_init__(self):
        if not self.question_id:
            self.question_id = f"q_{len(self.__class__.__dict__.get('_questions', [])) + 1}"


@dataclass
class MentorResource:
    resource_id: str = ""
    title: str = ""
    url: Optional[str] = None
    notes: str = ""

    def __post_init__(self):
        if not self.resource_id:
            self.resource_id = f"res_{len(self.__class__.__dict__.get('_resources', [])) + 1}"


@dataclass
class MentorFeedback:
    feedback_id: str = ""
    session_date: Optional[str] = None
    summary: str = ""
    rating: int = 0

    def __post_init__(self):
        if not self.feedback_id:
            self.feedback_id = f"fb_{len(self.__class__.__dict__.get('_feedbacks', [])) + 1}"


@dataclass
class MentorProgressReport:
    report_id: str = ""
    period_start: Optional[str] = None
    period_end: Optional[str] = None
    goals_reviewed: list = field(default_factory=list)

    def __post_init__(self):
        if not self.report_id:
            self.report_id = f"rpt_{len(self.__class__.__dict__.get('_reports', [])) + 1}"
