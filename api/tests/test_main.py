import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.mark.parametrize(
    "message,expected",
    [
        ("hello world", False),
        ("damn the world", True),
    ],
)
def test_check(client: TestClient, message: str, expected: bool):
    response = client.post("/check", json={"message": message})
    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.parametrize(
    "message,status",
    [
        ("", 422),
        ("#" * 300, 422),
    ],
)
def test_check_validation(client: TestClient, message: str, status: int):
    response = client.post("/check", json={"message": message})
    assert response.status_code == status


@pytest.mark.parametrize(
    "message,expected",
    [
        ("hello world", "hello world"),
        ("damn the world", "**** the world"),
    ],
)
def test_censor(client: TestClient, message: str, expected: str):
    response = client.post("/censor", json={"message": message})
    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.parametrize(
    "message,status",
    [
        ("", 422),
        ("#" * 300, 422),
    ],
)
def test_censor_validation(client: TestClient, message: str, status: int):
    response = client.post("/censor", json={"message": message})
    assert response.status_code == status


def test_health(client: TestClient):
    response = client.head("/health")
    assert response.status_code == 200
