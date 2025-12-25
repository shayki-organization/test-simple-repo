"""Pytest configuration for test-simple-repo."""

import pytest

from fastapi.testclient import TestClient

from test_simple_repo.app import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client."""
    return TestClient(app)
