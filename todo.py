from todo_manager import TodoManager
manager = TodoManager("todos.json")
#menu
while True:
    print("\n--- TODO APP ---")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Exit")
    choice =input('choose an option: ')
    try:
        choice = int(choice) 
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice ==1:
        print("Add todo selected")
        title =input("enter todo title:")
        new_task = manager.add_task(title)
        print(f"Task added: {new_task.id}. {new_task.title}")
    elif choice ==2:
        print("View todos selected")
        manager.view_tasks()
    elif choice ==3:
        print("Update todo selected") 
        try:
            task_id =int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid id. Please enter a number.")
            continue
        new_title = input("Enter new title (leave blank to keep current): ")
        completed_input = input("Is the task completed? (yes/no, leave blank to keep current): ")
        completed = None
        if completed_input.lower() == "yes":
            completed = True
        elif completed_input.lower() == "no":
            completed = False
        updated_task = manager.update_task(task_id, new_title if new_title else None, completed)
        if updated_task:
            print("Task updated successfully.")
        else:
            print("Task not found.")
    elif choice ==4:
        print("delete todo selected")
        try:
            delete_id =int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid id. Please enter a number.")
            continue
        if manager.delete_task(delete_id):
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    elif choice ==5:
        print("Exiting...")
        break       
    else:    
        print("Invalid choice. Please try again.")         