#!/usr/bin/python3

import requests


def top_ten(subreddit):
    '''
    GET/print top ten titles of first ten hot listings
    '''

    try:
        request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                               .format(subreddit), allow_redirects=False,
                               headers={'User-Agent': 'Betty'}).json()
        for m in request['data']['children']:
            print(m['data']['title'])
    except BaseException:
        print(None)
