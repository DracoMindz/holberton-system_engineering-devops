#!/usr/bin/pyhton3
""" Python script: uses REST API, for employee, return info about """
""" employee TODO list progress """

import requests
import sys

if __name__ == '__main__':

    """ employee information requests """
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])).json()
    employee_name = employee.get('name')

    """ todo information requests """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1])).json()
    tot_tasks = len(tasks)
    com_tasks = []
    for task in tasks:
        if task.get('completed') is True:
            com_tasks.append(task)
    tcom_tasks = len(com_tasks)

    """ Print the employee task data """
    print('Employee {} is done with tasks ({}/{}):'.
              format(employee_name, tcom_tasks, tot_tasks))
    for task in com_tasks:
        print('\t {}'.format(task.get('title')))
