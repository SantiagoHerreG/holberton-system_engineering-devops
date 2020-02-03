#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]

    todos = requests.get("http://jsonplaceholder.typicode.com/\
todos?userId={}".format(param))
    user = requests.get("http://jsonplaceholder.typicode.com\
/users/{}".format(param))

    if len(user.json()):
        total = 0
        completed = 0
        comp_list = []
        for to_do in todos.json():
            total += 1
            if to_do.get("completed") is True:
                completed += 1
                comp_list.append(to_do.get("title"))

        print("Employee {} is done with tasks({}/{}):\
".format(user.json().get("name"), completed, total))
        for task in comp_list:
            print("\t{}".format(task))
