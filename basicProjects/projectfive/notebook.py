# ==============================================================================
#                  PROJECT 6: THE PERSISTENT SECRET NOTEBOOK
# ==============================================================================
from datetime import datetime

while True:
    print("\n---------------------------")
    print("------ ENGINE NOTEPAD -----")
    print("---------------------------")
    print("[A] Append Thought   | [R] Read History")
    print("[W] Overwrite Whole  | [E] Exit Notebook")
    print("---------------------------")
    
    choice = input("Enter operation to perform: ").upper().strip()
    
    match choice:
        case 'A':
            with open("thoughts.txt", "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_here = input("Enter your thoughts: ")
                file.write(f"Content: {write_here} | Logged: {timestamp}\n")
                print("New data appended, no previous data was harmed!")
                
        case 'R':
            print("\n--- READING DISK ENTRIES  ---")
            try:
                with open("thoughts.txt", "r") as file:
                    content = file.read()
                    
                    # Clean handle in case the file exists but has no text characters inside
                    if not content.strip():
                        print("Notice: File is blank. No thoughts logged yet.")
                    else:
                        print(content)
                        
            except FileNotFoundError:
                print("[-] System Notice: 'thoughts.txt' does not exist on disk yet. Log a thought first!")
                
        case 'W':
            confirm = input("WARNING: This wipes out ALL past entries. Proceed? (Y/N): ").upper().strip()
            if confirm != 'Y':
                print("Overwrite canceled. Safety sequence secure.")
                continue
                
            with open("thoughts.txt", "w") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                thoughts = input("Enter your new master thoughts: ")
                # Combined variables into one clean structural string block argument
                file.write(f"Content: {thoughts} | Logged: {timestamp}\n")
                print("Past data truncated. Fresh master log recorded successfully.")
                
        case 'E':
            print("Shutting down the persistent notebook portal. Stream closed securely.")
            break
            
        case _:
            print("[-] Error: Input option unrecognized.")