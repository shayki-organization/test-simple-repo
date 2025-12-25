"""Tests for test-simple-repo."""

import pytest

from test_simple_repo import __version__


def test_version() -> None:
    """Test version is set."""
    assert __version__ is not None


def test_health_check(client) -> None:
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_items(client) -> None:
    """Test listing items."""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_item(client) -> None:
    """Test creating an item."""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item"},
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"
