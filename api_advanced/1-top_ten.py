#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:reddit_top_ten:v1.0'}
    params = {'limit': 10}
    
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) > 0:
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print("")
    else:
        print("")
