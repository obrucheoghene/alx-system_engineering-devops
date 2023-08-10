#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all
    hot articles for a given subreddit
    """

    headers = {"User-Agent": "CustomUserAgent"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                post_data = post['data']
                hot_list.append(post_data['title'])
            after = data['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        except (KeyError, ValueError):
            return None
    else:
        return None
