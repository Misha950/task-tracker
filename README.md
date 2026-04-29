#Task Tracker
https://roadmap.sh/projects/task-tracker
# Task Tracker CLI

A command-line tool to track and manage your tasks.

## Requirements

- Python 3.x

## Usage

```bash
python task_cli.py <command> [arguments]
```

## Commands

| Command | Description |
|--------|-------------|
| `add <description>` | Add a new task |
| `update <id> <description>` | Update a task |
| `delete <id>` | Delete a task |
| `mark-in-progress <id>` | Mark task as in progress |
| `mark-done <id>` | Mark task as done |
| `list` | List all tasks |
| `list todo` | List todo tasks |
| `list in-progress` | List tasks in progress |
| `list done` | List completed tasks |

## Examples

```bash
python task_cli.py add "Buy groceries"
python task_cli.py mark-done 1
python task_cli.py list done
```
