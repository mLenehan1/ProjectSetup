# Project Setup

This python script is used to begin new projects.

Functionality:
- Create a project
  - Create local project directory
  - Initialise local git repo
  - Create GitHub repo
  - Push first commit with an empty "README"
- Delete a project
  - Delete local project directory
  - Delete local git repo
  - Delete GitHub repo
- List a users git repos

Usage:

In order to use this script:

1. Create an environment variable named 'GIT_KEY' with your GitHub access token.

```
    export GIT_KEY="YourAccessTokenHere"
```

2. Change the 'localProjectDirectory' value to your desired project directory
location.
