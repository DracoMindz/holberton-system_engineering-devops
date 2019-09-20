#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    '''
    GET list of all hot articles use a recursive
    '''

    if len(hot_list) == 0:
        return None
    try:
        req = requests.get('https://www.reddit.com/r/{}/hot.json?after=after'
                           .format(subreddit), allow_redirects=False,
                           headers={'User-Agent': 'Betty'}).json()
        hotAfter = req['data']['after']
        for m in req['data']['children']:
            hot_list.append(m['data']['title'])
        return recurse(subreddit, hot_list, hotAfter)
    except BaseException:
        print(None)
