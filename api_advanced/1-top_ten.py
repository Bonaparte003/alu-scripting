#!/usr/bin/python3
"""function that fetches from reddit"""
import requests


def top_ten(subreddit):
    """"function that fetches data """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    headers = {
            'User-Agent': 'MyAPI/0.1'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9",
            allow_redirects=False,
            headers=headers
            )
    if r.status_code != 200:
        print(None)
        return
    for child in r.json()["data"]["children"][1:]:
        print(child["data"]["title"])
