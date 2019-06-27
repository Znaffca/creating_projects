import os
import sys
from additionals import check, get_github_user, username, password, project_path


def create():
    try:
        project_name = str(sys.argv[1])
    except IndexError:
        print("Please type your project name first!")

    if check(project_name) != project_name:
        print(check(project_name))
        exit(0)

    project_name = check(project_name)
    try:
        os.makedirs(project_path + "/" + project_name)
        print("Project folder generate succesfull!")
    except FileExistsError:
        print("That project already exists!")

    user = get_github_user(username, password)
    repo = user.create_repo(project_name)
    print("Succesfully created repository {} for user {}".format(repo.name, user.name))


if __name__ == "__main__":
    create()
