# ==============================================================================
#                       THE TERMINAL TASK MATRIX
# ==============================================================================

tasks = []

id_counter = 1

while True:
    print("\n=====================================")
    print("         TASK MATRIX ENGINE          ")
    print("=====================================")
    print("[V] View Matrix  | [A] Add Task")
    print("[C] Complete Task| [D] Delete Task")
    print("[E] Exit Engine")
    print("=====================================")

    choice = input("Enter Operation: ").upper().strip()

    match choice:
        case 'V':
            if len(tasks) == 0:
                print("No tasks yet!")
            else :
                for task in tasks:
                    print(f"ID: {task['id']} | Task: {task['title']} | Status: {task['status']}")
        case 'A':
            title_input = input("Enter Task Description: ").strip()

            if not title_input:
                print("Validation error! task input cannot be empty")
                continue

            new_task = {
                "id" : id_counter,
                "title": title_input,
                "status": "Pending"
            }
            tasks.append(new_task)
            id_counter += 1
        case 'E':
            print("Shutting the program down")
            break
        case 'C' :
            if len(tasks) == 0:
               print("No tasks to be found")
               continue
            try:
               target_id = int(input("Enter task id number: "))
               found = False

               for task in tasks:
                   if task['id'] == target_id:
                      task['status'] = "Complete"
                      found = True
                      break
                
               if not found:
                       print("Could not find task with that id, view the list again")
            except ValueError:
                print("Error on input")
        case 'D':
            if len(tasks) == 0:
               print("No tasks to be found")
               continue
            try:
               target_id = int(input("Enter task id number: "))
               found = False

               for task in tasks:
                   if task['id'] == target_id:
                     
                    tasks.remove(task)
                    found = True
                    break
                
               if not found:
                       print("Could not find task with that id, view the list again")
            except ValueError:
                print("Error on input")
        case _:
            print("[-] Error: Operational option index unrecognized.")