#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles, and prints
a sorted count of given keywords
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords
    """
    
    headers = {'User-Agent': 'CustomUserAgent'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            all_titles = [post['data']['title'].lower() for post in posts]
            all_words = ' '.join(all_titles).split()

            word_counter = Counter(all_words)

            for word in word_list:
                count = word_counter.get(word.lower(), 0)
                if count > 0:
                    print(f"{word.lower()}: {count}")
            
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after)
        except (KeyError, ValueError):
            return
    else:
        return
