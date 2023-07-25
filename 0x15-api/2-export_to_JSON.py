#!/usr/bin/python3
"""Export data to CSV"""
import csv
import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        with urllib.request.urlopen(user_url) as user_response:
            user_data = json.loads(user_response.read().decode())

        with urllib.request.urlopen(todo_url) as todo_response:
            todo_data = json.loads(todo_response.read().decode())

        employee_id = user_data.get('id')
        employee_username = user_data.get('username')

        file_name = f'{employee_id}.json'

        tasks_json = {
            employee_id: [
                {
                    "task": task.get('title'),
                    "completed": task.get("completed"),
                    "username": employee_username
                }
                for task in todo_data
            ]
        }
        with open(file_name, 'w', encoding='UTF8') as jsonfile:
            json.dump(tasks_json,  jsonfile)

    except urllib.error.URLError as e:
        print(e)
    except ValueError as e:
        print("Error: Invalid response from the API")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <emplyee_id>")
    else:
        employee_id = sys.argv[1]
        try:
            employee_id = int(employee_id)
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer")
