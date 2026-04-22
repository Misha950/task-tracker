import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def add_task(description):
    tasks = load_tasks()
    task = {
        "id": next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задачу додано (ID: {task['id']})")

