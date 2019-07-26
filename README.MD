# SAMPLE SCRIPT TO AUTOMATE CREATING PROJECTS IN PYTHON

### How it suposed to work - what does that script should do:
That simple script should automate creating and removing projects process in local computer and Github. It starts in os shell and has two simple commands

## But first...

### SetUp
Run set_up.py to configure script to work. It create (if not exists) folder for your future projects and add some env vars to your .bashrc file (like basic info about your github account). It also contais a basic password verify -> when your password contain characters which are special for Linux shell, an "\\" is added before that char to make the readable

## COMMANDS

### CREATE `project_name`

- create project folder in specified directory 
- check if specified project name contains invalid chars
- add a few basic files like .gitignore, requirements, README
- create a virtualenv with the name convention `{project_name}_env`
- init git repository and add all created files to git
- create remote repository with name like local project
- add local repo to remote and push project to github
- run Visual Studio Code with recently created project

### DELETE `project_name`

- remove local repository
- delete remote Github repository
- delete created virtualenv

### Changes in the future

- add functionality to install on Windows-based systems
- modify creating virtualenv depending of using virtualenv engine

### WARNING
Shell function requires to virtualenvwrapper installed on your pc. 

### How to run this repository in your PC:
1. Clone repository on your pc
2. Navigate to project
3. Install requirements using `pip install -r requirements.txt`
4. Run setup_py using python set_up.py, enter name of your workspace folder, and your github credentials.

To create new project in python just write:

```create project_name```

To remove existing project just use:

```delete project_name```

Enjoy :)