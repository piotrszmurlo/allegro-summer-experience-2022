from http import HTTPStatus
import sys
import json
from pytest import fixture
import responses
sys.path.insert(0, 'src')
from constants import API_URL, API_KEY
from api import GithubAPIWrapper


@fixture()
def mock_user_api_response():
    with open("./tests/resources/mock_user_api_response.json", encoding="utf-8") as f:
        return json.load(f)


@fixture()
def mock_user_repos_api_response():
    with open("./tests/resources/mock_user_repos_api_response.json", encoding="utf-8") as f:
        return json.load(f)


@fixture()
def mock_languages_responses():
    with open("./tests/resources/mock_repo_api_response.json", encoding="utf-8") as f:
        return json.load(f)


@responses.activate
def test_get_user_repo_details(mock_user_repos_api_response, mock_languages_responses):
    repos_url = f'{API_URL}/users/piotrszmurlo/repos'
    responses.add(responses.GET, repos_url, json=mock_user_repos_api_response, status=HTTPStatus.OK, headers={'Authorization': f'token {API_KEY}'})
    language_urls = [f'{API_URL}/repos/piotrszmurlo/ARKO21Z/languages',
                    f'{API_URL}/repos/piotrszmurlo/BD1/languages',
                    f'{API_URL}/repos/piotrszmurlo/SOI21Z/languages']
    for i, url in enumerate(language_urls):
        responses.add(responses.GET, url, json=mock_languages_responses[i], status=HTTPStatus.OK, headers={'Authorization': f'token {API_KEY}'})
    expected_result = {"ARKO21Z":{"Assembly":11005,"C":5673,"CMake":919},
                        "BD1":{},
                        "SOI21Z":{ "C": 185293,"C++": 11933,"Shell": 1313
                        }}
    api = GithubAPIWrapper()
    result = api.get_user_repo_details('piotrszmurlo')
    assert expected_result == result


@responses.activate
def test_get_user_detais(mock_user_repos_api_response, mock_user_api_response, mock_languages_responses):
    user_url = f'{API_URL}/users/piotrszmurlo'
    repos_url = f'{user_url}/repos' 
    responses.add(responses.GET, user_url, json=mock_user_api_response, status=HTTPStatus.OK, headers={'Authorization': f'token {API_KEY}'})
    responses.add(responses.GET, repos_url, json=mock_user_repos_api_response, status=HTTPStatus.OK, headers={'Authorization': f'token {API_KEY}'})
    language_urls = [f'{API_URL}/repos/piotrszmurlo/ARKO21Z/languages',
                    f'{API_URL}/repos/piotrszmurlo/BD1/languages',
                    f'{API_URL}/repos/piotrszmurlo/SOI21Z/languages']
    for i, url in enumerate(language_urls):
        responses.add(responses.GET, url, json=mock_languages_responses[i], status=HTTPStatus.OK, headers={'Authorization': f'token {API_KEY}'})
    api = GithubAPIWrapper()
    result = api.get_user_details('piotrszmurlo')
    expected_result = {
                    "login":"piotrszmurlo",
                    "name":"Piotr Szmurło",
                    "bio":"CS student @ Warsaw University of Technology",
                    "languages":{"Assembly":11005,"C":190966,
                        "CMake":919,"Shell":1313,"C++":11933}
                    }
    assert expected_result == result