#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on
    a given subreddit or 'None' if it doesn't exist."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if response.status_code != 200:
        print("None")  # Print "None" if the subreddit does not exist
        return

    results = response.json().get("data", {}).get("children", [])
    if not results:
        print("None")
        return

    for post in results:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
