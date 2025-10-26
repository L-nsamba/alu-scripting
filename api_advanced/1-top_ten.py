#!/usr/bin/python3
"""
1-top_ten
Queries the Reddit API and prints the titles of the first 10
hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "CustomUserAgent"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Invalid subreddit → print None
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        children = data.get("data", {}).get("children", [])

        if not children:
            print(None)
            return

        for child in children:
            print(child.get("data", {}).get("title"))

    except Exception:
        print(None)
