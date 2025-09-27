import json
import os

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["completed"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

# Mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {index} marked as completed.")
    except IndexError:
        print("Error: Task number does not exist.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task deleted: {removed['task']}")
    except IndexError:
        print("Error: Task number does not exist.")

# Menu-driven program
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to mark completed: "))
                complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
