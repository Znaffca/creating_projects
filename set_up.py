import os
from getpass import getpass
from additionals import check_password


def set_up():
    workspace = input("Select name for your workspace folder: ")
    username = input("Type your github username: ")
    password = getpass(prompt="Type your github password: ")
    home = os.environ["HOME"]
    export_lines = [
        "export WORKSPACE=$HOME/{}".format(workspace),
        'export GITHUB_USER="{}"'.format(username),
        'export GITHUB_PASS="{}"'.format(check_password(password)),
        "source {}/.my_command.sh".format(os.path.abspath(os.path.dirname(__file__))),
    ]

    if not os.path.exists("{}/{}".format(home, workspace)):
        os.makedirs(home + "/" + workspace)
        print("Main projects folder {} created succesfully".format(workspace))

    with open(f"{home}/.bashrc", "a+") as f:
        r = open(f"{home}/.bashrc", "r")
        content = r.read()
        for i in export_lines:
            if i not in content:
                f.write(i + "\n")
                print("{} succesfully added to file".format(i))
            else:
                print("Content {} already exists in requested file".format(i))
        r.close()
        f.close()


if __name__ == "__main__":
    set_up()
