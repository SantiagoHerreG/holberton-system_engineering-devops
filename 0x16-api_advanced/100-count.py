#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, list_res=[]):

    flag = 0
    headers = {'User-Agent': "sherre"}
    if len(list_res) == 0:
        res = requests.get("https://www.reddit.com/r/" + subreddit +
                           "/hot.json", headers=headers, allow_redirects=False)
        flag = 1
        for _ in range(len(word_list)):
            list_res.append(0)
    else:
        res = requests.get("https://www.reddit.com/r/" + subreddit,
                           headers=headers, allow_redirects=False)

    if res.json().get("data").get("children") is not None:
        for value in res.json().get("data").get("children"):
            title = value.get("data").get("title")
            for j in range(len(word_list)):
                i = 0
                while i >= 0:
                    i = title.find(" " + word_list[j] + " ", i + 1)
                    if i > 0:
                        list_res[j] += 1
        if res.json().get("data").get("after") is not None:
            if flag:
                subreddit = subreddit + "/hot.json?after=" +\
                                 res.json().get("data").get("after")
            else:
                subreddit = subreddit[:-9] +\
                                 res.json().get("data").get("after")
            return count_words(subreddit, word_list, list_res)

    for i in range(len(list_res)):
        big = max(list_res)
        idx = list_res.index(big)
        print(word_list[idx] + ":" + " " + str(list_res[idx]))
        list_res[idx] = -1
    return
