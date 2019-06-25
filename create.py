import os
import sys
from github import Github

project_path = os.environ["WORKSPACE"]
username = os.environ["GITHUB_USER"]
password = os.environ["GITHUB_PASS"]


def create():
    try:
        folder_name = str(sys.argv[1])
    except IndexError:
        print("Please type your project name first!")
    except FileExistsError:
        print("You just wrote incorrect character. Please type again")
        exit(0)

    os.makedirs(project_path + "/" + folder_name)
    print("Project folder generate succesfull!")

    user = Github(login_or_token=username, password=password).get_user()
    repo = user.create_repo(folder_name)
    print("Succesfully created repository {} for user {}".format(repo.name, user.name))


if __name__ == "__main__":
    create()
