import os

TODO_FILE = 'todo_data.txt'

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
    else:
        print("Your task List:")
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}. {todo}")

def add_todo(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added task: {task}")

def update_todo(index, new_task):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid task index.")
        return
    todos[index - 1] = new_task
    save_todos(todos)
    print(f"Updated task #{index}: {new_task}")

def delete_todo(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid task index.")
        return
    removed_todo = todos.pop(index - 1)
    save_todos(todos)
    print(f"Deleted task: {removed_todo}")

def main():
    while True:
        print("\nto-do List Application")
        print("1. List all ")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_todos()
        elif choice == '2':
            task = input("Enter the new task: ")
            add_todo(task)
        elif choice == '3':
            list_todos()
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the updated task: ")
            update_todo(index, new_task)
        elif choice == '4':
            list_todos()
            index = int(input("Enter the index of the task to delete: "))
            delete_todo(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
