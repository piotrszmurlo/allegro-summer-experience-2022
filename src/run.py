from api import GithubAPI
from pprint import pprint
def main():
    api = GithubAPI()
    res = api.get_user_details('piotrszmurlo')
    res2 = api.get_user_repo_details('piotrszmurlo')
    pprint(res)
    pprint(res2)

if __name__ == '__main__':
    main()