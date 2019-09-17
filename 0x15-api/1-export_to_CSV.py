#!/usr/bin/python3
"""
Python script: export data in CSV format
"""


if __name__ == "__main__":
    import csv
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

    # Export data in the CSV format
    data_row = [[user_id,
                username,
                task.get('completed'),
                task.get('title')]
                for task in taskList]

    # Insert csv data row
    with open('{}.csv'.format(user_id), 'w') as m:
        writeFile = csv.writer(m, quoting=csv.QUOTE_ALL)
        writeFile.writerows(data_row)
