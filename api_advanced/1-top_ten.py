#!/usr/bin/python3
"""
Reddit API Query Module
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:reddit-api-client:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                print("None")
                return

            for post in posts:
                title = post['data']['title']
                print(title)

        else:
            # If status code is not 200 (could be 404, 302, etc.)
            print("None")

    except (requests.RequestException, KeyError, ValueError):
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
