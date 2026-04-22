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


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = []
    for t in tasks:
        if t["id"] != task_id:
            new_tasks.append(t)
    if len(new_tasks) == len(tasks):
        print(f"Задача з ID {task_id} не знайдена.")
        return
    save_tasks(new_tasks)
    print(f"Задачу з ID {task_id} видалено.")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["description"] = new_description
            t["updatedAt"] = now()
            save_tasks(tasks)
            print(f"Задачу з ID {task_id} оновлено.")
            return
    print(f"Задача з ID {task_id} не знайдена.")        


def mark_task(task_id, status):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = status
            t["updatedAt"] = now()
            save_tasks(tasks)
            print(f"Задачу з ID {task_id} позначено як {status}.")
            return
    print(f"Задача з ID {task_id} не знайдена.")
            