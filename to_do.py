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
            add = input("Enter your task name: ")
            to_do_list.append(add)
            print("Task added !")

        elif action == 2:
            old_task = input("Which task you want to update?: ")
            if old_task in to_do_list:
                new_task = input("Enter new task: ")
                idx = to_do_list.index(old_task) 
                to_do_list[idx] = new_task        
                print("Task updated!")
            else:
                print("This task is not in list.")

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