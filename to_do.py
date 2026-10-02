import pandas as pd 

def to_do():
    to_do_list = []
    print("--- Welcome to the To Do app ---")
    
    while True:
        print("\n1. Add Task  2. Update Task  3. View Tasks  4. Delete Task  5. Exit")
        try:
            action = int(input("Enter what you want to do : "))
        except ValueError:
            print("Invalid! Enter only numbers (1-5) .")
            continue

        if action == 1:
            task = input("Enter task name: ").strip()
            if task:
                to_do_list.append(task)
                print(f" Task '{task}' added successfully!")
            else:
                print("Task name cannot be empty.")

        elif action == 2:
            if not to_do_list:
                print("List is empty! Add some tasks first.")
                continue
            
            task_num = input("Enter task number to update (or type task name): ").strip()
            
            if task_num.isdigit() and 1 <= int(task_num) <= len(to_do_list):
                idx = int(task_num) - 1
                new_task = input("Enter new task: ").strip()
                to_do_list[idx] = new_task
                print(" Task updated successfully!")
            elif task_num in to_do_list:
                idx = to_do_list.index(task_num)
                new_task = input("Enter new task: ").strip()
                to_do_list[idx] = new_task
                print(" Task updated successfully!")
            else:
                print("Task not found in list.")

        elif action == 3:
            if not to_do_list:
                print("Empty list! ")
            else:
                print("\n--- Today's Task Report (Pandas DataFrame) ---")
                df = pd.DataFrame(to_do_list, columns=["Task Name"])
                df.index = df.index + 1  
                print(df)

        elif action == 4:
            delete_val = input("Which task you want to delete? : ")
            if delete_val in to_do_list:
                to_do_list.remove(delete_val)
                print("Task deleted !")
            else:
                print("Task is not found !")

        elif action == 5:
            print("Closing app. Bye!")
            break

        else:
            print("Invalid action! Try Again!!")

to_do()
