#!/usr/bin/python3
"""Function that fetches top 10 hot posts from a subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    headers = {'User-Agent': 'MyAPI/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    fetched_data = requests.get(url, headers=headers, allow_redirects=False)
    
    if fetched_data.status_code == 200:
        results = fetched_data.json()
        data = results['data']['children']
        
        for i in range(min(9, len(data))):
            print(data[i]['data']['title'])
    else:
        print(None)
