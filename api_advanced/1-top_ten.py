#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.

Usage:
    from 1-top_ten import top_ten
    top_ten('programming')
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    If the subreddit is invalid or an error occurs, print nothing.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALUProject/1.0 (by student)"}
    params = {"limit": 10}

    try:
        resp = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if resp.status_code != 200:
            return
        children = resp.json().get("data", {}).get("children", [])
        for post in children[:10]:
            print(post.get("data", {}).get("title"))
    except requests.exceptions.RequestException:
        # Network-related errors (connection, timeout, etc.)
        return
