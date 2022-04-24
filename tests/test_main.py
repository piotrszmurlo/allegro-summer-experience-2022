import sys
from fastapi.testclient import TestClient
sys.path.insert(0, 'src')
from main import app


client = TestClient(app)


def test_user_details():
    response = client.get('/user/piotrszmurlo')
    assert response.status_code == 200


def test_user_details_nonexistent():
    response = client.get('/user/...')
    assert response.status_code == 404


def test_user_details_null_data():
    response = client.get('/user/kokos')
    assert response.status_code == 200


def test_repos_details():
    response = client.get('/repos/piotrszmurlo')
    assert response.status_code == 200


def test_repos_details_null_data():
    response = client.get('/repos/kokos')
    assert response.status_code == 200


def test_repos_details_nonexistent():
    response = client.get('/repos/...')
    assert response.status_code == 404