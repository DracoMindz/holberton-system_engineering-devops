#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    '''
    GET total number of subscribers to reddit
    '''

    try:
        request = requests.get('https://www.reddit.com/r/{}/about.json'.
                               format(subreddit),
                               headers={'User-Agent': 'Betty'}).json()
        return request['data']['subscribers']
    except KeyError:
        return 0
