# === Stage 51: Add unit tests for search and filter behavior ===
# Project: MentorBoard
import unittest


class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        from mentorboard.models.session import Session
        self.sessions = [
            Session(id="s1", title="Python basics", goal="Learn syntax", topics=["python"], status="completed"),
            Session(id="s2", title="OOP design", goal="Design classes", topics=["oop"], status="planned"),
            Session(id="s3", title="Testing", goal="Write tests", topics=["testing"], status="in_progress"),
        ]

    def test_search_by_title(self):
        result = [s for s in self.sessions if "Python" in s.title]
        self.assertEqual(result, [self.sessions[0]])

    def test_filter_by_status(self):
        active = [s for s in self.sessions if s.status == "in_progress"]
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].id, "s3")

    def test_combined_search_and_filter(self):
        result = [s for s in self.sessions if "Testing" in s.title and s.status != "completed"]
        self.assertEqual(result, [self.sessions[2]])


if __name__ == "__main__":
    unittest.main()
