#!/usr/bin/pyhton3
""" Python script: uses REST API, for employee, return info about """
""" employee TODO list progress """

import requests
import sys

if __name__ == '__main__':

    """ Url information """
    url = 'https://jsonplaceholder.typicode.com'
    req = requests.get(url)

    """ employee information requests """
    employee = requests.get(https: // jsonplaceholder.
                            typicode.com/users?sys.argv[1]).json()
    employee_name = employee.get('name')

    """ todo information requests """
    tasks = requests.get(https: // jsonplaceholder.
                         typicode.com/todos?sys.argv[1]).json()
    tot_tasks = len(tasks)
    com_tasks = tasks.get('completed')

    while req is not None:

        print('Employee {} is done with tasks {}/{}:'.
              format(employee_name, com_tasks / tot_tasks))
        print('\t{}" "'.format(com_tasks.get('title')))
