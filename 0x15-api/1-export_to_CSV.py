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

    name = user.json().get("name")
    if name:
        string = ""
        for to_do in todos.json():
            string += "\"{}\",\"{}\",\"{}\",\"{}\"\n\
".format(param, name, to_do.get("completed"), to_do.get("title"))
        with open("{}.csv".format(param), encoding="UTF", mode="w") as f:
            f.write(string)
