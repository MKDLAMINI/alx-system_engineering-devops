#!/usr/bin/python3
"""
write a function that prints 10 hot posts in a given subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    user = {'User-Agent': 'MyRedditApp/0.0.1'}
    url = f'https://www.reddit.co /r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print("None")
    except requests.RequestException:
        print("None")



if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Please provide a subreddit name")
