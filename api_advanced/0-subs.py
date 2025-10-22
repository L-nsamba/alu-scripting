#!/usr/bin/python3
import requests
import string

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python:subscribers:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the subreddit exists (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception:
        return 0

# Example usage:
print(number_of_subscribers("python"))  # Should return the subscriber count
print(number_of_subscribers("nonexistentsubreddit12345"))  # Should return 0
