#!/usr/bin/python3
"""
function that fetches from reddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that fetches all hot articles recursively
    """
    headers = {'User-Agent': 'MyAPI/0.1.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    fetched_data = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)
    status = fetched_data.status_code

    if status == 200:
        results = fetched_data.json()
        data = results['data']['children']
        for item in data:
            hot_list.append(item['data']['title'])

        after = results['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
