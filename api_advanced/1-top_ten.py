#!/usr/bin/python3
"""
Function that queries Reddit API
"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:top_ten:v1.0"}
    params = {"limit": 10}
    
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        print("None")
