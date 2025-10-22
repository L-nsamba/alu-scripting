#!/usr/bin/python3
"""
Module that contains a recursive function to fetch all hot article titles
from a given subreddit using the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetches hot article titles from a subreddit."""
    if hot_list is None:
        hot_list = []

    headers = {
        'User-Agent': 'python:recurse_hot:v1.0 '
                      '(by Leon-Nsamba)'
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    for post in data.get('children', []):
        hot_list.append(post['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
