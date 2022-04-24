import requests
from functools import reduce
from operator import add
from collections import Counter
from constants import API_KEY, API_URL


class GithubAPIWrapper():


    def get_user_repo_details(self, username: str) -> dict:
        """Returns user's repository details: repositories names with languages usage in bytes.
            Throws requests.exceptions.HTTPError if occurred in API call"""
        res = self._request_user_repos(username)
        res.raise_for_status()
        user_repo_details = {}
        for element in res.json():
            languages = self._get_languages(element['languages_url'])
            languages.raise_for_status()
            user_repo_details[element['name']] = languages.json()
        return user_repo_details


    def get_user_details(self, username: str) -> dict:
        """Returns user's details: login, name, languages (aggregated) with usage in bytes.
            Throws requests.exceptions.HTTPError if occurred in API call"""
        res = self._request_user_details(username)
        res.raise_for_status()
        res = res.json()
        user_details = {}
        elements_to_extract = ('login', 'name', 'bio')
        for element in elements_to_extract:
            user_details[element] = res[element]
        res = self._request_user_repos(username)
        res.raise_for_status()
        repo_details = []
        res = res.json()
        if res:
            for element in res:
                languages = self._get_languages(element['languages_url'])
                languages.raise_for_status()
                repo_details.append(languages.json())
            aggregated_repos_data = dict(reduce(add, map(Counter, repo_details)))
            user_details['languages'] = aggregated_repos_data
        return user_details


    def _request_user_repos(self, username: str) -> requests.Response:
        return requests.get(f'{API_URL}/users/{username}/repos', headers={'Authorization': f'token {API_KEY}'})


    def _request_user_details(self, username: str) -> requests.Response:
        return requests.get(f'{API_URL}/users/{username}', headers={'Authorization': f'token {API_KEY}'})


    def _get_languages(self, languages_url: str) -> requests.Response:
        return  requests.get(languages_url, headers={'Authorization': f'token {API_KEY}'})