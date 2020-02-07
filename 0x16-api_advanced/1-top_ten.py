#!/usr/bin/python3
""" HTTP requests to Reddit API
"""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': "sherre"}
    res = requests.get("https://www.reddit.com/r/" + subreddit +
                       "/hot.json?limit=10",
                       headers=headers, allow_redirects=False)
    try:
        if res.json().get("data").get("children") is not None:
            for value in res.json().get("data").get("children"):
                print(value.get("data").get("title"))
            return
        else:
            print("None")
    except:
        print("None")
