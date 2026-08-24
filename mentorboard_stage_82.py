# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: MentorBoard
def demo():
    from mentorboard import MentorBoard
    board = MentorBoard("Alice", "Bob", "Python basics")
    board.set_goal("Learn to use decorators")
    board.ask_question("How do @staticmethod differ from static methods?")
    board.add_resource("Python docs", "https://docs.python.org/3/reference/datamodel.html")
    board.take_feedback("Great progress, keep going!")
    board.update_progress(75)
    print(board.generate_progress_report())
    print("Demo complete.")
