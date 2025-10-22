#!/usr/bin/python3
"""Reddit API Query Module"""
import requests

def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts"""
    url=f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers={'User-Agent':'python:reddit-api-client:v1.0'}
    try:
        response=requests.get(url,headers=headers,allow_redirects=False)
        if response.status_code==200:
            data=response.json()
            posts=data['data']['children']
            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
