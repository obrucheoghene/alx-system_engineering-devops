import requests


def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests issues
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the URL for the subreddit's API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            data = response.json()
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
