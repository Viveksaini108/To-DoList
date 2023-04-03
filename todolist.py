import json
tasks = []  # initialize empty list to store tasks

while True:
    # print menu options
    print("\n1. Add task\n2. View tasks\n3. Mark task as complete\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task description: ")
        tasks.append(task)  # add task to list
        print("Task added successfully!")
        
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("Task list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
                
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            index = int(input("Enter task number to mark as complete: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
            else:
                tasks.pop(index)  # remove task from list
                print("Task marked as complete.")
                
    elif choice == '4':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")

# load existing tasks from file, if available
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

while True:
    # print menu options
    print("\n1. Add task\n2. View tasks\n3. Mark task as complete\n4. Save and exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task description: ")
        tasks.append({"task": task, "completed": False})  # add task to list
        print("Task added successfully!")
        
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("Task list:")
            for i, task in enumerate(tasks):
                status = "X" if task["completed"] else " "
                print(f"{i+1}. [{status}] {task['task']}")
                
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            index = int(input("Enter task number to mark as complete: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
            else:
                tasks[index]["completed"] = True  # mark task as completed
                print("Task marked as complete.")
                
    elif choice == '4':
        # save tasks to file
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("Tasks saved to file. Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")
# load existing tasks from file, if available
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

while True:
    # print menu options
    print("\n1. Add task\n2. View tasks\n3. Mark task as complete\n4. Delete task\n5. Save and exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task description: ")
        tasks.append({"task": task, "completed": False})  # add task to list
        print("Task added successfully!")
        
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("Task list:")
            for i, task in enumerate(tasks):
                status = "X" if task["completed"] else " "
                print(f"{i+1}. [{status}] {task['task']}")
                
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            index = int(input("Enter task number to mark as complete: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
            else:
                tasks[index]["completed"] = True  # mark task as completed
                print("Task marked as complete.")
    
    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            index = int(input("Enter task number to delete: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
            else:
                tasks.pop(index)  # remove task from list
                print("Task deleted.")
                
    elif choice == '5':
        # save tasks to file
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("Tasks saved to file. Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")
