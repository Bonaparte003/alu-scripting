#!/usr/bin/python3
"""function that fetches API reddit in rercusion"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    # Set up the URL to make a request to Reddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Set the parameters for pagination (after indicates the next page)
    params = {'limit': 100, 'after': after}
    
    # Make the request to the Reddit API
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data')
        
        # Add the titles of the current page's hot articles to the hot_list
        hot_list += [child['data']['title'] for child in data['children']]
        
        # Check if there's another page to fetch, using 'after'
        after = data.get('after')
        if after is None:
            # Base case: no more pages to fetch
            return hot_list
        else:
            # Recursive case: fetch the next page
            return recurse(subreddit, hot_list, after)
    
    except Exception as e:
        # Handle any exceptions, such as connection errors or JSON parsing errors
        return None
