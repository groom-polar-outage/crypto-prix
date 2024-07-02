import pytest


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("COINGECKO_API_KEY", "<change-me>")
    monkeypatch.setenv("TSDB_URL", "<change-me>")
    monkeypatch.setenv("TSDB_TOKEN", "<change-me>")
    monkeypatch.setenv("TSDB_ORG", "FOO")
    monkeypatch.setenv("TSDB_BUCKET", "BAR")
    monkeypatch.setenv("TIMEZONE", "Europe/Prague")
