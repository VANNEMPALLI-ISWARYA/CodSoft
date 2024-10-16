# Simple To-Do List Application

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    """Main function to run the To-Do List application."""
    tasks = []
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task description: ")
            tasks.append(task)
            print(f'Task "{task}" added successfully!')

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                try:
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f'Task "{removed_task}" deleted successfully!')
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
