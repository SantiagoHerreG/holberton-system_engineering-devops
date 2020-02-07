#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[]):

    flag = 0
    headers = {'User-Agent': "sherre"}
    if len(hot_list) == 0:
        res = requests.get("https://www.reddit.com/r/" + subreddit +
                           "/hot.json", headers=headers, allow_redirects=False)
        flag = 1
    else:
        res = requests.get("https://www.reddit.com/r/" + subreddit,
                           headers=headers, allow_redirects=False)
    try:
        if res.json().get("data").get("children") is not None:
            for value in res.json().get("data").get("children"):
                hot_list.append(value.get("data").get("title"))
            if res.json().get("data").get("after") is not None:
                if flag:
                    subreddit = subreddit + "/hot.json?after=" +\
                                    res.json().get("data").get("after")
                else:
                    subreddit = subreddit[:-9] +\
                                    res.json().get("data").get("after")
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return hot_list
    except:
        return None
