#!/usr/bin/python3

import requests
import sys


def top_ten(subreddit):
    '''
    GET list of all hot articles use a recursive
    '''

    try:
        request = requests.get('https://www.reddit.com/r/{}/hot.json'
                               .format(subreddit), allow_redirects=False,
                               headers={'User-Agent': 'Betty'}).json()
        for m in request['data']['children']:
            print(m['data']['title'])
    except BaseException:
        print(None)
