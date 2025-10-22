#!/usr/bin/python3
"""
Module to query Reddit API for subreddit subscriber count
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0.0 (by /u/youruser)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            # Extract subscriber count from the response
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except (requests.RequestException, ValueError, KeyError):
        return 0
