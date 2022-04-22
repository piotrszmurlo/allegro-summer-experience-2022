from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200


def test_root():
    response = client.get('/')
    assert response.status_code == 200


def test_user_details():
    response = client.get('/user/piotrszmurlo')
    assert response.status_code in (200, 403)


def test_user_details_nonexistent():
    response = client.get('/user/piotrszmurlo')
    assert response.status_code in (403, 404)


def test_repos_details():
    response = client.get('/repos/piotrszmurlo')
    assert response.status_code in (200, 403)