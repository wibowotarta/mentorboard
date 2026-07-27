# === Stage 57: Add structured result objects for command handlers ===
# Project: MentorBoard
class SessionResult:
    """Structured result returned by every MentorBoard command handler."""

    def __init__(self, status="ok", message="", data=None):
        self.status = status
        self.message = message
        self.data = data or {}

    @property
    def success(self):
        return self.status in ("ok", "created", "updated", "deleted")

    def to_dict(self):
        d = {"status": self.status, "message": self.message}
        if self.data is not None:
            d["data"] = self.data
        return d

    def __repr__(self):
        return f"SessionResult(status={self.status!r}, message={self.message!r})"


class SessionError(SessionResult):
    """Raised when a handler encounters an unexpected or invalid input."""

    def __init__(self, code="BAD_REQUEST", detail="", **kwargs):
        super().__init__(status=code, message=detail)
