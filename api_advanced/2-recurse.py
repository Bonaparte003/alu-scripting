#!/usr/bin/python3
"""function that fetches API reddit in rercurse mode"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

        if response.status_code != 200:
            return None
        data = response.json().get('data')
        hot_list += [child['data']['title'] for child in data['children']]
        after = data.get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except Exception:
        return None
