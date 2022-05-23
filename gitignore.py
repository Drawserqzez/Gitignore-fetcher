#!/usr/bin/python3

import requests
import sys

try:
    url = 'https://raw.githubusercontent.com/github/gitignore/main/'
    projectType = sys.argv[1]
    url += projectType[0].upper() + projectType[1:] + '.gitignore'

    print("Getting gitignore file for project type " + projectType)

    response = requests.get(url)

    if response.ok:
        with open("./.gitignore", "wb") as file:
            file.write(response.content)
        print("Gitignore file created")
    else:
        print('Invalid project type: ' + projectType)

except IndexError as indexError: 
    print("You need to specify a language or a project type")
except Exception as e: 
    print("Could not get the gitignore file :(")
    print(e)

