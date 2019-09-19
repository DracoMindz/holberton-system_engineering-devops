#!/usr/bin/python3

import requests
import sys


def top_ten(subreddit):
    '''
    GET/print top ten titlesof first ten hot listings
    '''

    try:
        request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                               format(subreddit), allow_redirects=False,
                               headers={'User-Agent': 'Betty'}).json()
        for m in request['data']['titles']:
            print(m['data']['titles'])
    except KeyError:
        return ('None')
