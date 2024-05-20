#!/usr/bin/python3
'''
gather employee data from API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            ask = requests.get('{}/users/{}'.format(REST_API, id)).json()
            assign_ask = requests.get('{}/todos'.format(REST_API)).json()
            employee_name = ask.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, assign_ask))
            fin_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(fin_tasks),
                    len(tasks)
                )
            )
            if len(fin_tasks) > 0:
                for task in fin_tasks:
                    print('\t {}'.format(task.get('title')))
