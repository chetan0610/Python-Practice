"""
MiniProject02_TodoList.py
To-Do List Manager: Add, Remove, Mark Completed, Save Automatically.
"""
import os

FILE_NAME = "todo.txt"

def load_tasks():
    """Loads tasks into a list."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Saves tasks from a list into the file."""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')

def main():
    """Main loop for the To-Do list."""
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
            
        print("\n1. Add Task | 2. Mark Complete | 3. Delete Task | 4. Exit")
        choice = input("Choice: ").strip()
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(f"[ ] {task}")
            save_tasks(tasks)
        elif choice == '2':
            idx = int(input("Task number to complete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx] = tasks[idx].replace("[ ]", "[X]")
                save_tasks(tasks)
        elif choice == '3':
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()