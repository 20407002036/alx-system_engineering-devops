#!/usr/bin/python3

import sys
import requests

def fetch_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = base_url + str(employee_id) + '/todos'

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)
    except ValueError as ve:
        print("Error decoding JSON:", ve)
        sys.exit(1)

    usr_response = requests.get(base_url)
    usr_data = usr_response.json()


    employee_name = todos[0]['name']
    total_tasks = len(todos)
    completed_tasks = [task['title'] for task in todos if task['completed']]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    """
    The script cannot run if impoted.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID should be an integer.")
        sys.exit(1)

    fetch_todo_progress(int(employee_id))
