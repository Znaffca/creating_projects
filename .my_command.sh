#!/usr/bin/env python


function create() {
    cd $SCRIPT_FOLDER
    python3 create.py $1
    cd $WORKSPACE/$1

    #create virtualenv
    mkvirtualenv "$1_env"
    deactivate

    #initialize local git repository
    git init

    # add some basic files
    touch README.MD requirements.txt
    cp $SCRIPT_FOLDER/.gitignore $WORKSPACE/$1

    # commit and create connection with the remote repository
    git add .
    git commit -m "Create project - initial commit"
    git remote add origin https://github.com/Znaffca/$1.git
    git push -u origin master

    #open specified project in Visual Studio Code
    echo "Opening Visual Studio Code"
    code .
    exit

}

function delete() {
    # move to directory stores python files
    cd $HOME/.local/bin
    python3 remove.py $1
    
    # go back to home dir
    cd $HOME
    rmvirtualenv "$1_env"
}