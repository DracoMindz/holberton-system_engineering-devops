#!/usr/bin/python3
"""
Python script: exports data in JSON format
"""
if __name__ == "__main__":
    import json
    import requests

    # url
    url = 'https://jsonplaceholder.typicode.com'

    # Employee information requests
    employee = requests.get('{}/users'.format(url).json()
    employee_list = employee

    # Todo information requests
    for user in employee_list:
        tasks = requests.get('{}/todos?userId={}'.
                             format(url, user.get('id'))).json()
        taskList += tasks

    # Export json formatted data in json file
    jsonDataDict = {user.get('id'): [{"task": task.get('title'),
                                     "completed": task.get('completed'),
                                     "username": task.get('username')}
                                     for task in taskList]}

    # Insert json data row
    with open('todo_all_employees.json', 'w') as mfile:
        json.dump(jsonDataDict, mfile)
