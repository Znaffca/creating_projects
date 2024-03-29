import os
import shutil
import sys
from additionals import get_github_user, project_path, username, password
import github


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

    g_user = get_github_user(username, password)
    try:
        repo = g_user.get_repo(name=project_name)
        repo.delete()
        print("Repository {} deleted from {} account".format(project_name, g_user.name))
    except github.GithubException:
        print("No matches repo found in {} profile...".format(g_user.name))
        exit(0)


if __name__ == "__main__":
    remove()
