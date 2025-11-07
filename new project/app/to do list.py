def show_menu():
    print("\nTO-DO LIST MENU")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks yet! You're all caught up.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter new task: ")
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if len(tasks) > 0:
        try:
            num = int(input("\nEnter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program
tasks = []
running = True
print("Welcome to To-Do List Manager!")

while running:
    show_menu()
    choice = input("\nChoose option (1-4): ")

    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("\nGoodbye!")
        running = False
    else:
        print("Invalid choice, please select 1-4.")