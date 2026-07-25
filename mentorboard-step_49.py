# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: MentorBoard
import pytest
from mentorboard.models.session import Session, SessionStatus
from datetime import datetime

def test_update_status_to_invalid_raises():
    session = Session(id="s1", title="Test", status=SessionStatus.COMPLETED)
    with pytest.raises(Exception):
        session.update(status="invalid")


def test_delete_session_removes_from_store():
    from mentorboard.store.session_store import SessionStore
    store = SessionStore()
    s = Session(id="d1", title="Delete Me", status=SessionStatus.ACTIVE)
    store.add(s)
    assert len(store.get_all()) == 1
    store.delete("d1")
    assert len(store.get_all()) == 0


def test_update_preserves_existing_fields():
    session = Session(id="u2", title="Original", status=SessionStatus.ACTIVE,
                      date=datetime(2024, 1, 1), goals=["Goal A"])
    updated = session.update(status=SessionStatus.COMPLETED)
    assert updated.status == SessionStatus.COMPLETED
    assert updated.title == "Original"
    assert updated.date.year == 2024
    assert len(updated.goals) == 1


def test_delete_nonexistent_session_raises():
    from mentorboard.store.session_store import SessionStore
    store = SessionStore()
    with pytest.raises(Exception):
        store.delete("nonexistent_id")
