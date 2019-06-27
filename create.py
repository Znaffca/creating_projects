import os
import sys
import re
from github import Github

project_path = os.environ["WORKSPACE"]
username = os.environ["GITHUB_USER"]
password = os.environ["GITHUB_PASS"]


def check(char):
    regex = re.compile("[@!#$%^&*()<>?/\\|}{~:]")
    if regex.search(char) is None:
        return char
    return (
        "Incorrect project name. Please enter the name using only alphanumeric chars."
    )


def get_github_user(username, password):
    return Github(login_or_token=username, password=password).get_user()


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
