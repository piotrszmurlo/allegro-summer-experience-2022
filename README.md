# allegro-summer-experience-2022

My email in recruitment process: `piotr.szmurlo7@gmail.com`

# Used technologies

* Python 3.9.12

* FastAPI 0.75.2

* requests 2.27.1

* pytest 7.1.2, responses 0.20.0

# Getting started

Create a virtual environment:

`python3 -m venv ./venv`

Activate the venv:

`.\venv\Scripts\Activate.ps1` in PowerShell

`.\venv\Scripts\activate.bat` in cmd.exe

` source ./venv/bin/activate` in bash/zsh

Install dependencies in venv:

`pip install -r requirements.txt`

Unauthorized calls to Github API get only 60 req/hour. Authenticating requests:

Set `API_KEY` constant in `src/constants.py` to your Github personal access token in order to raise Github's API rate limit to 5000 req/hour

Testing:

`pytest` in order to run tests (some will fail if rate limit is exceeded)

To run the http server:

`cd src`

`uvicorn main:app`

The server should now be up.
Try visiting `http://127.0.0.1:8000/user/allegro` or `http://127.0.0.1:8000/repos/allegro`.

# Simplifications, assumptions, possible improvements

* Caching Github API's responses

* Sending requests in an asynchronous manner to get the results faster (fetching languages data for each repo is slow when synchronous)

* More elegant way of providing Personal Access Token

* More tests covering all corner cases

* Cleaner test code

* Mocking api responses for test_main.py tests

    - Assumed that an user named 'kokos' will not ever have any repositories (empty repository test, he did not have any since creating the account - 12 years...)

* Separating pytest fixtures, github api calling functions if there were more
