#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetches hot article titles from a subreddit."""
    if hot_list is None:
        hot_list = []

    # Set custom User-Agent to avoid 429 Too Many Requests
    headers = {'User-Agent': 'Leon Nsamba alu reddit project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Handle invalid subreddit
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    # Extract titles and append to the list
    for post in data.get('children', []):
        hot_list.append(post['data']['title'])

    # Check if there is a next page
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
