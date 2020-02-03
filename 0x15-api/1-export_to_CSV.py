#!/usr/bin/python3
"""Write a Python script that takes data from an API
and creates a CSV file with it
"""

import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]

    todos = requests.get("http://jsonplaceholder.typicode.com/\
todos?userId={}".format(param))
    user = requests.get("http://jsonplaceholder.typicode.com\
/users/{}".format(param))

    if len(user.json()) and len(todos.json()):
        string = ""
        for to_do in todos.json():
            string += "\"{}\",\"{}\",\"{}\",\"{}\"\n\
".format(user.json().get("id"), user.json().get("username"),
         to_do.get("completed"), to_do.get("title"))
        with open("{}.csv".format(param), mode="w") as f:
            f.write(string)
