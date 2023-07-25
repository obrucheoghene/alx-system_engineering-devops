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

        file_name = f'{employee_id}.csv'
        with open(file_name, 'w', encoding='UTF8') as csvfile:
            csv_writer = csv.writer(csvfile)

            for task in todo_data:
                csv_writer.writerow([
                    employee_id,
                    employee_username,
                    task.get('completed'),
                    task.get('title')
                    ])

    except urllib.error.URLError as e:
        print(e)
    except ValueError as e:
        print("Error: Invalid response from the API")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <emplyee_id>")
    else:
        empployee_id = sys.argv[1]
        try:
            empployee_id = int(empployee_id)
            get_employee_todo_progress(empployee_id)
        except ValueError:
            print("Error: Employee ID must be an integer")
