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
    employee = requests.get('{}/users'.format(url))
    employeeList = employee.json()

    # Todo information requests
    list_of_tasks = []
    for user in employeeList:
        todoList = requests.get('{}/todos?userId={}'.
                                format(url, user.get('id'))).json()
        list_of_tasks += todoList

    # Export json formatted data in json file
    jsonDataDict = {user.get('id'): [{"task": task.get('title'),
                                     "username": task.get('username'),
                                     "completed": task.get('completed')}
                                     for task in list_of_tasks]
                    for user in employeeList}

    # Insert json data row
    with open('todo_all_employees.json', 'w') as mfile:
        json.dump(jsonDataDict, mfile)
