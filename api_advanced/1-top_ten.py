#!/usr/bin/python3
"""function that fetches from reddit"""
import requests


def top_ten(subreddit):
    """function that fetches top 10 hottest posts"""
    headers = {'User-Agent': 'MyAPI/0.1.1'}
    url = "https://www.reddit.com/r/{}.json?limit=9".format(subreddit)
    fetched_data = requests.get(url, headers=headers, allow_redirects=False)
    status = fetched_data.status_code
    if status == 200:
        results = fetched_data.json()
        data = results['data']['children']
        for i in range(9):
            print(data[i]['data']['title'])
    else:
        print(None)
