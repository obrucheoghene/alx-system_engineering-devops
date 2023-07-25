#!/usr/bin/python3
"""Export data to CSV"""
import csv
import json
import os
import sys
import urllib.request


def get_employee_todo_progress():
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    filename = 'todo_all_employees.json'
    all_employees_todos = {}

    try:
        with urllib.request.urlopen(users_url) as users_response:
            users_data = json.loads(users_response.read().decode())

        for user in users_data:
            employee_id = user.get('id')
            employee_username = user.get('username')
            todo_url = f'{base_url}/todos?userId={employee_id}'

            with urllib.request.urlopen(todo_url) as todo_response:
                todo_data = json.loads(todo_response.read().decode())
            tasks_json = [
                    {
                        "task": task.get('title'),
                        "completed": task.get("completed"),
                        "username": employee_username
                    }
                    for task in todo_data
                ]

            all_employees_todos[employee_id] = tasks_json

        with open(filename, 'w', encoding='UTF8') as jsonfile:
            json.dump(all_employees_todos,  jsonfile)

    except urllib.error.URLError as e:
        print(e)
    except ValueError as e:
        print("Error: Invalid response from the API")


if __name__ == "__main__":

    try:
        get_employee_todo_progress()
    except ValueError:
        print("Error: Employee ID must be an integer")
