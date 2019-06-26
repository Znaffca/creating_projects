import os
import shutil
import sys
from github import Github
import github

project_path = os.environ["WORKSPACE"]
username = os.environ["GITHUB_USER"]
password = os.environ["GITHUB_PASS"]


def remove():
    try:
        project_name = sys.argv[1]
        shutil.rmtree(project_path + "/" + project_name)
        print("Succesfully removed {} !".format(project_name))
    except (IndexError, FileExistsError):
        print(
            "An unexpected error occured. Please make sure that you wrote a correct name or project folder was already deleted"
        )
        exit(0)

    g_user = Github(login_or_token=username, password=password).get_user()
    try:
        repo = g_user.get_repo(name=project_name)
        repo.delete()
        print("Repository {} deleted from {} account".format(project_name, g_user.name))
    except github.GithubException:
        print("No matches repo found in {} profile...".format(g_user.name))
        exit(0)


if __name__ == "__main__":
    remove()
