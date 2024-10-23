#!/usr/bin/python3
"""
function that fetches data from a
reddit API.


"""
import requests


def number_of_subscribers(subreddit):
    """function that fetches data"""
    headers = {'User-Agent': 'MyAPI/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    fetched_data = requests.get(url, headers=headers, allow_redirects=False)
    results = fetched_data.json()
    status = fetched_data.status_code
    if status == 200:
        subscribers = results['data']['subscribers']
    else:
        subscribers = 0
    return subscribers
