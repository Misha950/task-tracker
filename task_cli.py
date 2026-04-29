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
            

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("Немає задач.")
        return
    for t in tasks:
        print(f"ID: {t['id']} | {t['description']} | Статус: {t['status']} | Створено: {t['createdAt']} | Оновлено: {t['updatedAt']}")
  

def main():
    args = sys.argv[1:]

    if not args:
        print("Будь ласка, введіть команду.")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Вкажи опис задачі. Приклад: python task_cli.py add 'Моя задача'")
            return
        add_task(" ".join(args[1:]))
    elif command == "delete":
        if len(args) < 2:
            print("Вкажи ID задачі для видалення. Приклад: python task_cli.py delete 1")
            return
        delete_task(int(args[1]))
    elif command == "update":
        if len(args) < 3:
            print("Вкажи ID задачі та новий опис. Приклад: python task_cli.py update 1 'Новий опис'")
            return
        update_task(int(args[1]), " ".join(args[2:]))
    elif command == "mark-in-progress":
        if len(args) < 2:
            print("Вкажи ID задачі для позначення як 'in-progress'. Приклад: python task_cli.py mark-in-progress 1")
            return
        mark_task(int(args[1]), "in-progress")
    elif command == "mark-done":
        if len(args) < 2:
            print("Вкажи ID задачі для позначення як 'done'. Приклад: python task_cli.py mark-done 1")
            return
        mark_task(int(args[1]), "done")
    elif command == "list":
        if len(args) > 1:
            list_tasks(args[1])
        else:
            list_tasks()
    else:
        print("Невідома команда.")    
    

if __name__ == "__main__":
    main()