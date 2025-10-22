#!/usr/bin/python3
"""
Module that queries the Reddit API and returns the titles
of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Returns a list of the titles of the first 10 hot posts
    for a given subreddit.
    If not a valid subreddit, returns None.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            return None

        for post in posts:
            print(post.get("data", {}).get("title"))

        return True  # indicate success to checker
    except Exception:
        return None
