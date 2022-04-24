# allegro-summer-experience-2022

My email in recruitment process: `piotr.szmurlo7@gmail.com`

# Getting started

Create a virtual environment:

`python3 -m venv ./venv`

Activate the venv:

`.\venv\Scripts\Activate.ps1` in PowerShell

`.\venv\Scripts\activate.bat` in cmd.exe

`./venv/bin/activate` in bash/zsh

Install dependencies in venv:

`pip install -r requirements.txt`

Unauthorized calls to Github API get only 60 req/hour. Authenticating requests:

Set `API_KEY` constant in `src/constants.py` to your Github personal access token in order to raise Github's API rate limit to 5000 req/hour

Testing:

`pytest` in order to run tests (some will fail if rate limit is exceeded)

To run the http server:

`cd src`

`uvicorn main:app`

Try visiting `http://127.0.0.1:8000/user/allegro` or `http://127.0.0.1:8000/repos/allegro`.

# Simplifications, assumptions, possible improvements

Things that could be added:

Caching Github API's responses

Sending requests in an asynchronous manner to get the results faster

More tests covering all corner cases 
