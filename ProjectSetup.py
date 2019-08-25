from sys import argv
from os import mkdir, chdir, system, environ
from github import Github
import click

g = Github(environ.get('GIT_KEY'))
user = g.get_user()

def createProject(project_name):
    """
    Create a new project directory given a project name
    """
    try:
        mkdir(project_name)
        print ("Directory Created")
    except FileExistsError:
        print ("Directory already exists")
        renamePrompt()

def createGitRepo():
    """
    Create a new git repository
    """
    print("Test")

def createGitHubRepo():
    """
    Create a new GitHub repository
    """
    print("Test")

def removeProject():
    """
    Remove a project repository
    """
    print("Test")

def listProjects():
    """
    Lists all GitHub repositories
    """
    for repo in user.get_repos():
            print(repo.name)
            print(repo.git_url)

def renamePrompt():
    """
    Prompt user to rename the directory
    """
    print ("Would you like to rename? [Y/n]")
    userChoice = input()
    if userChoice == "Y":
        print("Enter new directory name: ")
        dirName = input()
        return dirName
    elif userChoice == "n":
        print ("Cancelling Project Creation")
        exit()
    else: 
        print ("Invalid Input")
        renamePrompt()

@click.command()
@click.option('--create', '-c', help='Create a new project', is_flag=True)
@click.option('--git', '-g', help='Create a new git/GitHub repository', is_flag=True)
@click.option('--remove', '-r', help='Remove a project', is_flag=True)
@click.option('--list', '-l', help='List existing GitHub repositories', is_flag=True)
@click.argument('project_name', required=False)
def main(create, git, remove, list, project_name):
    if create:
        
    elif git:
        try:
            print("Test")
        except FileExistsError:
            print("Test")
    elif remove:
        try:
            print("Test")
        except FileExistsError:
            print("Test")
    elif list:
        listProjects()
    else:
        print(
            "Please enter a valid option.\nFor usage try \"ProjectSetup.py --help\""
            )

if __name__ == "__main__":
    main()