#!/usr/bin/python3
""" HTTP requests to Reddit API
"""
import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': "sherre"}
    res = requests.get("https://www.reddit.com/r/" + subreddit + "/about.json", headers=headers)
    return (res.json().get("data").get("subscribers"))
