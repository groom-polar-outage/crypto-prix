import pytest


@pytest.fixture
def mock_env(monkeypatch):
    # openssl rand -hex 32
    monkeypatch.setenv("FASTAPI_USERS_SECRET","<change-me>")
    monkeypatch.setenv("TSDB_URL", "<change-me>")
    monkeypatch.setenv("TSDB_TOKEN", "<change-me>")
    monkeypatch.setenv("TSDB_ORG", "FOO")
    monkeypatch.setenv("TSDB_BUCKET", "BAR")
    monkeypatch.setenv("TIMEZONE", "Europe/Prague")
