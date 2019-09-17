#!/usr/bin/python3
"""
Python script: exports data in JSON format
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    # User ID
    user_id = sys.argv[1]

    # Employee information requests
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(sys.argv[1])).json()
    username = employee.get('username')

    # Todo information requests
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1])).json()
    taskList = tasks

    # Export json formatted data in json file
    jsonDataDict = {user_id: [{"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username}
                              for task in taskList]}

    # Insert json data row
    with open('{}.json'.format(user_id), 'w') as mfile:
        json.dump(jsonDataDict, mfile)
