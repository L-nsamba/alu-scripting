#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or an error occurs, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.topten:v1.0 (by /u/you)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Treat non-200 or redirect responses as invalid subreddit
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)
    except (requests.exceptions.RequestException, Value
