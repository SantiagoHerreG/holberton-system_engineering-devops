#!/usr/bin/python3
"""Write a Python script that takes data from an API
and creates a JSON file with it
"""

import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]

    todos = requests.get("http://jsonplaceholder.typicode.com/\
todos?userId={}".format(param))
    user = requests.get("http://jsonplaceholder.typicode.com\
/users/{}".format(param))

    name = user.json().get("username")
    if len(user.json()) and len(todos.json()):
        string = "{{\"{}\": [".format(param)
        flag = 0
        for to_do in todos.json():
            if flag:
                string += ", "
            string += "{{\"username\": \"{}\", \"task\": \"{}\", \"completed\"\
: {}}}".format(name, to_do.get("title"), "true" if to_do.get("complete\
d") is True else "false")
            flag = 1
        string += "]}"
        with open("{}.json".format(param), mode="w") as f:
            f.write(string)
