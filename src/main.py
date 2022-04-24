from requests.exceptions import HTTPError
from api import GithubAPIWrapper
from fastapi import FastAPI, HTTPException


app = FastAPI()
api = GithubAPIWrapper()


@app.get('/')
async def root():
    return 'Try /repos/{username} or /user/{username}'


@app.get('/user/{username}')
async def user_details(username):
    try:
        response = api.get_user_details(username)
    except HTTPError as e:
        if e.response.status_code == 403:
            raise HTTPException(status_code=403, detail='HTTP error: github api rate limit exceeded')
        elif e.response.status_code == 404:
            raise HTTPException(status_code=404, detail='HTTP error: username not found')
        else:
            raise HTTPException(status_code=400, detail='HTTP error occurred')
    return response


@app.get('/repos/{username}')
async def repos_details(username):
    try:
        response = api.get_user_repo_details(username)
    except HTTPError as e:
        if e.response.status_code == 403:
            raise HTTPException(status_code=403, detail='HTTP error: github api rate limit exceeded')
        elif e.response.status_code == 404:
            raise HTTPException(status_code=404, detail='HTTP error: username not found')
        else:
            raise HTTPException(status_code=400, detail='HTTP error occurred')
    return response
