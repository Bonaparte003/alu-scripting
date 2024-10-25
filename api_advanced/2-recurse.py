#!/usr/bin/python3
"""A script that recursively queries the Reddit API and returns a list of
hot post titles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and
    returns a list of hot post titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The parameter for pagination, indicating
        the next page of results.

    Returns:
        list: A list containing the titles of hot posts,
        or None if the subreddit is invalid.
    """
    # Set up the URL to make a request to Reddit's hot posts API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        # Make the request to the Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

        # Check if the response status code is not 200 (OK)
        if response.status_code != 200:
            return None

        # Parse the JSON response and get the data
        data = response.json().get('data')

        # Append the titles of the hot posts to the hot_list
        hot_list += [child['data']['title'] for child in data['children']]

        # Get the 'after' parameter for pagination
        after = data.get('after')

        # If 'after' is None, return the hot_list, otherwise, recurse
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

    except Exception as e:
        # Return None in case of any exception
        return None
