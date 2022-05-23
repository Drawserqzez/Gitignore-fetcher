#!/usr/bin/python3

import requests
import sys

try:
    url = 'https://raw.githubusercontent.com/github/gitignore/main/' # static link to github repo =)

    projectType = sys.argv[1]
    url += projectType[0].upper() + projectType[1:] + '.gitignore' # Most of the time, the project's first letter is capitalised

    print("Getting gitignore file for project type " + projectType)

    response = requests.get(url)

    if response.ok:
        with open("./.gitignore", "wb") as file:
            file.write(response.content)
        print("Gitignore file created")
    else:
        print('Invalid project type: ' + projectType)

except IndexError as indexError: # If sys.argv[1] doesn't exist
    print("You need to specify a language or a project type")
except Exception as e: # any and all other errors
    print("Could not get the gitignore file :(")
    print(e)

