#!/usr/bin/python3
"""function that fetches from reddit"""
import requests


def top_ten(subreddit):
    """"function that fetches data """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    headers = {'User-Agent': 'MyAPI/0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    r = requests.get(url, allow_redirects=False, headers=headers)
    if r.status_code != 200:
        print(None)
        return
    for child in r.json()["data"]["children"][1:]:
        print(child["data"]["title"])
