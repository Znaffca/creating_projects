import os
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


def check_password(password):
    invalid_chars = "~`#$&*()\\|[]{};'<>/?!"
    new_pass = ""
    for i in password:
        if i in invalid_chars:
            new_pass += f"\\{i}"
        else:
            new_pass += i
    return new_pass
