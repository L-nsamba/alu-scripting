#!/usr/bin/python3
"""
Recursive function to get all hot article titles from a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries Reddit API to get all hot articles from a subreddit

    Args:
        subreddit (str): The subreddit to search
        hot_list (list): List to accumulate article titles (default empty)
        after (str): Pagination token for next page (default None)

    Returns:
        list: List of hot article titles, or None if subreddit is invalid
    """
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set headers to avoid redirects and identify our bot
    headers = {
        'User-Agent': 'python:reddit_recursive_scraper:v1.0 (by /u/your_username)'
    }

    # Add pagination parameter if we have an 'after' token
    params = {'limit': 100}  # Maximum posts per request
    if after:
        params['after'] = after

    try:
        # Make the API request - don't follow redirects automatically
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # If we get a redirect (status 301 or 302), subreddit doesn't exist
        if response.status_code in [301, 302]:
            return None

        # If we get any other non-200 status, subreddit doesn't exist or other error
        if response.status_code != 200:
            return None

        # Parse the JSON response
        data = response.json()

        # Extract posts from the current page
        posts = data['data']['children']

        # If no posts found and this is the first page, return None
        if not posts and not after:
            return None

        # Add titles from current page to our list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Get the pagination token for next page
        next_after = data['data']['after']

        # If there's a next page, make recursive call
        if next_after:
            return recurse(subreddit, hot_list, next_after)
        else:
            # No more pages, return the accumulated list
            return hot_list

    except Exception:
        # If any error occurs (network, JSON parsing, etc.), return None
        return None
