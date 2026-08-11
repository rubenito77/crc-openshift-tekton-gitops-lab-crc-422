from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "OpenShift Tekton GitOps en CRC" in response.text
    assert "V1 - Version 1.0.0" in response.text


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready() -> None:
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_info() -> None:
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json() == {
        "name": "app-demo",
        "version": "1.0.0",
        "environment": "dev",
        "git_commit": "local",
    }
