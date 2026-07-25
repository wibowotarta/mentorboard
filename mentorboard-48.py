# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: MentorBoard
import unittest
from datetime import date, timedelta
from mentorboard.models.session import Session


class TestSession(unittest.TestCase):
    def _make(self, goals=None, questions=None, resources=None, feedback=None):
        return Session(
            title="Test",
            date=date.today(),
            duration_minutes=30,
            notes="",
            goals=goals or [],
            questions=questions or [],
            resources=resources or [],
            feedback=feedback or "",
        )

    def test_valid_creation(self):
        s = self._make(goals=["Learn Python"], questions=["How to use lists?"])
        self.assertEqual(s.title, "Test")
        self.assertEqual(len(s.goals), 1)
        self.assertEqual(len(s.questions), 1)
        self.assertIsInstance(s.date, date)
        self.assertGreaterEqual(s.duration_minutes, 0)

    def test_empty_fields(self):
        s = self._make()
        self.assertEqual(s.title, "Test")
        self.assertEqual(s.goals, [])
        self.assertEqual(s.questions, [])
        self.assertEqual(s.resources, [])
        self.assertEqual(s.feedback, "")

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            Session(title="Bad", duration_minutes=-1)


if __name__ == "__main__":
    unittest.main()
