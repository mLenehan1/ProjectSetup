from sys import argv
from os import mkdir, chdir, system, environ
from shutil import rmtree
from github import Github, GithubException
from click import command, option, argument

g = Github(environ.get('GIT_KEY'))
user = g.get_user()
localProjectDirectory = '/home/michael/Documents/Projects'


def createProject(project_name):
    """
    Create a new project directory given a project name
    """
    try:
        chdir(localProjectDirectory)
        mkdir(project_name)
        print("Directory Created")
        createGitRepo(project_name)
    except FileExistsError:
        print("Directory already exists")
        createProject(renamePrompt())


def createGitRepo(project_name):
    """
    Create a new git repository
    """
    gitHubPath = user.login + '/' + project_name
    createLocalGitRepo(project_name)
    createGitHubRepo(project_name)
    system('touch README.md')
    system('git add README.md')
    system('git commit -m "Initialised Repo"')
    system('git remote add origin https://github.com/' + gitHubPath)
    system('git push -u origin master')
    system('code .')
    print("Operation Complete")
    exit()


def createLocalGitRepo(project_name):
    """
    Create a new local git repository
    """
    print("Would you like to create a Git repo? [Y/n]")
    userChoice = input().lower()
    if userChoice == "y":
        chdir(project_name)
        system('git init')
    elif userChoice == "n":
        print("Project Creation Completed")
        exit()
    else:
        print("Invalid Input")
        createLocalGitRepo(project_name)


def createGitHubRepo(project_name):
    """
    Create a new GitHub repository
    """
    print("Would you like to create a GitHub repo? [Y/n]")
    userChoice = input().lower()
    if userChoice == "y":
        try:
            user.create_repo(project_name, private=True)
            print("GitHub repo initialised")
        except GithubException:
            print("Directory Already Exists")
    elif userChoice == "n":
        print("Project Creation Completed")
        exit()
    else:
        print("Invalid Input")
        createGitHubRepo(project_name)


def removeProject(project_name):
    """
    Remove a project repository
    """
    removeGitProject(project_name)
    removeGitHubProject(project_name)
    print("Operation Complete")
    exit()


def removeGitProject(project_name):
    """
    Remove a project Git repository
    """
    print("Would you like to delete the project locally? [Y/n]")
    userChoice = input().lower()
    if userChoice == "y":
        try:
            chdir('/home/michael/Documents/Projects')
            rmtree(project_name)
            print("Local Directory Deleted")
        except FileNotFoundError:
            print("File Does Not Exist In the Specified Location")
            return False
    elif userChoice == "n":
        return False
    else:
        print("Invalid Input")
        removeGitProject(project_name)


def removeGitHubProject(project_name):
    """
    Remove a project GitHub repository
    """
    print("Would you like to delete the GitHub repo? [Y/n]")
    userChoice = input().lower()
    if userChoice == "y":
        try:
            g.get_repo(full_name_or_id=user.login+"/"+project_name).delete()
            print("GitHub Repo Deleted")
        except GithubException:
            print("GitHub Repo Does Not Exist")
    elif userChoice == "n":
        return False
    else:
        print("Invalid Input")
        removeGitHubProject(project_name)
    return True


def listProjects():
    """
    Lists all GitHub repositories
    """
    for repo in user.get_repos():
        print(repo.name + " | " + repo.git_url)


def renamePrompt():
    """
    Prompt user to rename the directory
    """
    print("Would you like to rename? [Y/n]")
    userChoice = input().lower()
    if userChoice == "y":
        print("Enter new directory name: ")
        dirName = input()
        return dirName
    elif userChoice == "n":
        print("Cancelling Project Creation")
        exit()
    else:
        print("Invalid Input")
        renamePrompt()


@command()
@option('--create', '-c', help='Create a new project', is_flag=True)
@option('--git', '-g', help='Create a new git/GitHub repository', is_flag=True)
@option('--remove', '-r', help='Remove a project', is_flag=True)
@option('--list', '-l', help='List existing GitHub repositories', is_flag=True)
@argument('project_name', required=False)
def main(create, git, remove, list, project_name):
    if create:
        createProject(project_name)
    elif git:
        createGitRepo(project_name)
    elif remove:
        removeProject(project_name)
    elif list:
        listProjects()
    else:
        print(
            "Please enter a valid option.\nFor usage try \"ProjectSetup.py --help\""
        )


if __name__ == "__main__":
    main()
