#!/usr/bin/python3
"""Query the Reddit API for hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, print None.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            print(None)
    except Exception:
        print(None)
