#!/usr/bin/python3
"""Write a Python script that takes data from an API
and creates a JSON file with it
"""

import requests

if __name__ == "__main__":

    users = requests.get("http://jsonplaceholder.typicode.com/users")

    flag_user = 0
    string = "{"

    for user in users.json():

        todos = requests.get("http://jsonplaceholder.typicode.com/\
todos?userId={}".format(user.get("id")))
        if flag_user:
            string += ", "
        flag_user = 1
        name = user.get("username")

        if name and len(todos.json()):

            flag = 0
            string += "\"{}\": [".format(user.get("id"))
            for to_do in todos.json():
                if flag:
                    string += ", "
                string += "{{\"username\": \"{}\", \"task\": \"{}\"\
, \"completed\": {}}}".format(name, to_do.get("title"), "true" if to_do.get("\
completed") is True else "false")
                flag = 1
            string += "]"
    string += "}"
    with open("todo_all_employees.json", mode="w") as f:
        f.write(string)
