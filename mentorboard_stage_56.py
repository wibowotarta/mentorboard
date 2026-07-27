# === Stage 56: Add compact error classes for domain failures ===
# Project: MentorBoard
class SessionError(Exception):
    """Raised when a mentoring session fails to load."""


class GoalValidationError(Exception):
    """Raised when goal text is empty, malformed, or unmeasurable."""


class QuestionConflictError(Exception):
    """Raised when duplicate questions are added."""


class ResourceMissingError(Exception):
    """Raised when a referenced resource cannot be resolved."""


class FeedbackRecencyError(Exception):
    """Raised when feedback is submitted outside the allowed window."""


class ProgressReportError(Exception):
    """Raised when progress data is inconsistent or incomplete."""
