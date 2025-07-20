# A To-Do List Manager
TASK_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    try:
        f= open(TASK_FILE, "r")
        return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
    
# Save tasks to the file
def save_tasks(tasks):
    f= open(TASK_FILE, "w")
    f.writelines([task + "\n" for task in tasks])

#add a  new task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")

#to display all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

#to delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    except IndexError:
        print("Invalid task number.")

def description():
    print("""
Usage:
    python todo-list.py add "Task description"
    python todo-list.py view
    python todo-list.py delete TASK_NUMBER
    """)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        description()
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) > 2:
            add_task(" ".join(sys.argv[2:]))
        elif command == "view":
            view_tasks()
        elif command == "delete" and len(sys.argv) == 3:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print("Task number must be an integer.")
        elif command == "delete":
            print("Enter Task number to delete")

        else:
            description()
