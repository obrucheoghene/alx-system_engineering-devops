#!/usr/bin/python3
"""
a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'CustomUserAgent'}
    url = f'https://www.reddit.com/r/{subreddit}/new.json'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for i in range(10):
                print(posts[i]['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
