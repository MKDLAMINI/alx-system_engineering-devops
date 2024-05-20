#!/usr/bin/python3
"""
write a script that records all tasks from all employees
"""
import requests
import sys
import json


if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(api)
    Users = res.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        api = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        api = api + '/todos/'
        res = requests.get(api)

        tasks = res.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
