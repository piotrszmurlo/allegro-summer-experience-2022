from pydantic import HttpUrl
from requests.exceptions import HTTPError
from api import GithubAPI
from fastapi import FastAPI

app = FastAPI()
api = GithubAPI()

@app.get("/")
async def root():
    return "Try /repos/{username} or /user/{username}"


@app.get("/repos/{username}")
async def user_details(username):
    try:
        response = api.get_user_details(username)
    except HTTPError:
        response = "A HTTPError occured (probably Github api rate limit reached or user does not exist)"
    return response


@app.get("/user/{username}")
async def user_details(username):
    try:
        response = api.get_user_repo_details(username)
    except HTTPError:
        response = "A HTTPError occured (probably Github api rate limit reached or user does not exist)"
    return response
