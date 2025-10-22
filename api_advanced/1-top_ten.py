#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Required by Reddit API
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If subreddit is invalid or request fails
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])
    if not data:
        print(None)
        return

    for post in data:
        print(post["data"]["title"])
