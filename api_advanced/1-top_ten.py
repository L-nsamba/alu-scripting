#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    
    Args:
        subreddit (str): The subreddit to search
    
    Returns:
        None: Prints titles or None
    """
    # Base URL for Reddit API
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set headers to avoid redirects and identify our bot
    headers = {
        'User-Agent': 'python:reddit_top_ten:v1.0'
    }
    
    # Parameters to get first 10 posts
    params = {'limit': 10}
    
    try:
        # Make the API request - don't follow redirects automatically
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # If we get a redirect or any non-200 status, subreddit doesn't exist
        if response.status_code != 200:
            print("None")
            return
        
        # Parse the JSON response
        data = response.json()
        posts = data['data']['children']
        
        # If no posts found, print None
        if not posts:
            print("None")
            return
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post['data']['title'])
            
    except Exception:
        # If any error occurs, print None
        print("None")
