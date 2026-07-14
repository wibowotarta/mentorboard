# === Stage 16: Add argparse support for the most common commands ===
# Project: MentorBoard
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="MentorBoard - Mentoring Session Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list
    l = subparsers.add_parser("list", help="List mentoring sessions")
    l.set_defaults(func=lambda _: display_sessions())

    # view
    v = subparsers.add_parser("view", help="View a session by ID")
    v.add_argument("session_id", help="Session identifier")
    v.set_defaults(func=lambda args: view_session(args.session_id))

    # create
    c = subparsers.add_parser("create", help="Create a new mentoring session")
    c.add_argument("--name", required=True, help="Session name")
    c.add_argument("--mentor", default="", help="Mentor name")
    c.add_argument("--mentee", default="", help="Mentee name")
    c.set_defaults(func=lambda args: create_session(args.name, args.mentor, args.mentee))

    # add_goal
    ag = subparsers.add_parser("add-goal", help="Add a goal to a session")
    ag.add_argument("session_id", help="Session identifier")
    ag.add_argument("--goal", required=True, help="Goal description")
    ag.set_defaults(func=lambda args: add_goal(args.session_id, args.goal))

    # add_question
    aq = subparsers.add_parser("add-question", help="Add a question to a session")
    aq.add_argument("session_id", help="Session identifier")
    aq.add_argument("--question", required=True, help="Question text")
    aq.set_defaults(func=lambda args: add_question(args.session_id, args.question))

    # add_resource
    ar = subparsers.add_parser("add-resource", help="Add a resource to a session")
    ar.add_argument("session_id", help="Session identifier")
    ar.add_argument("--url", required=True, help="Resource URL or path")
    ar.set_defaults(func=lambda args: add_resource(args.session_id, args.url))

    # feedback
    fb = subparsers.add_parser("feedback", help="Add feedback to a session")
    fb.add_argument("session_id", help="Session identifier")
    fb.add_argument("--message", required=True, help="Feedback message")
    fb.set_defaults(func=lambda args: add_feedback(args.session_id, args.message))

    # report
    r = subparsers.add_parser("report", help="Generate a progress report")
    r.add_argument("-o", "--output", default=None, help="Output file path (default: stdout)")
    r.set_defaults(func=lambda args: generate_report(args.output))

    return parser.parse_args()


if __name__ == "__main__":
    from MentorBoard import display_sessions, view_session, create_session, add_goal, \
        add_question, add_resource, add_feedback, generate_report
