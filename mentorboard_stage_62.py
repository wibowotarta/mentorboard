# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: MentorBoard
class ScoringEngine:
    """Simple scoring / priority recommendation for mentoring sessions."""

    def __init__(self):
        self.criterion_weights = {
            "goal_clarity": 0.25,
            "question_depth": 0.25,
            "resource_relevance": 0.20,
            "feedback_quality": 0.15,
            "progress_visibility": 0.15,
        }

    def score_session(self, session: dict) -> float:
        """Score a session based on its attributes."""
        total = sum(self.criterion_weights.values())
        weighted_score = 0.0
        for criterion, weight in self.criterion_weights.items():
            raw_score = session.get(criterion, {}).get("score", 0)
            normalized = min(raw_score / max(self._max_scores[criterion], 1), 1.0)
            weighted_score += weight * normalized
        return round(weighted_score, 3)

    def recommend_improvement(self, session: dict) -> str:
        """Suggest the weakest area to improve."""
        scores = {}
        for criterion in self.criterion_weights:
            raw = session.get(criterion, {}).get("score", 0)
            scores[criterion] = min(raw / max(self._max_scores[criterion], 1), 1.0)

        weakest_criterion = min(scores, key=scores.get)
        return f"Focus on improving {weakest_criterion}."

    def generate_priority_report(self, sessions: list[dict]) -> list[dict]:
        """Return sessions sorted by score with priority labels."""
        scored = []
        for session in sessions:
            score = self.score_session(session)
            if score >= 0.85:
                priority = "high"
            elif score >= 0.70:
                priority = "medium"
            else:
                priority = "low"
            scored.append({"session": session, "score": score, "priority": priority})

        return sorted(scored, key=lambda x: x["score"], reverse=True)

    def _max_scores(self):
        if not hasattr(self, "_cache"):
            self._cache = {
                "goal_clarity": 10,
                "question_depth": 10,
                "resource_relevance": 10,
                "feedback_quality": 10,
                "progress_visibility": 10,
            }
        return self._cache
