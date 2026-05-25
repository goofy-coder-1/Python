# =============================================
#            J S O N   D A T A B A S E
# =============================================

import json

try:
    with open("profile_database.json", "r") as file:
        students = json.load(file)
        print(f"Database loaded successfully. Detected {len(students)} student record arrays.")
except (FileNotFoundError, json.JSONDecodeError):
    students = []
    print("Error tracking")
    
while True:
    print("\n=====================================")
    print("      STUDENT PARSER DB ENGINE       ")
    print("=====================================")
    print("[V] View Records   | [A] Add New Student")
    print("[E] Save & Exit")
    print("=====================================")

    choice = input("Enter operation to perform: ").upper()
    match choice:
        case 'V':
            print("-------- Current Student Database --------------")
            if len(students) == 0:
                print("Current list does not have any data of any student")
            else:
                for student in students:
                    print(f"ID: {student['id']} | Name: {student['name']} | Course: {student['course']} | GPA: {student['gpa']:.2f}")
            print("--------------------------------------------------")

        case 'A':
            print("------------ Add students -------------")
            try:
                name = input("Enter your name: ")
                if not name:
                    print("name can't be empty")
                course = input("Enter course: ")
                gpa = float(input("Enter GPA: "))

                if gpa > 4.0 or gpa < 0.0:
                    print("Invalid gpa")
                    continue
                
                new_id = len(students) + 1

                new_student = {
                    "id": new_id,
                    "name": name,
                    "course": course,
                    "gpa": gpa
                }
                students.append(new_student)
                print(f"Success: Packed and staged record for '{name}' under reference index ID: {new_id}.")

            except ValueError:
                print("Data type error")
        
        case 'E':
            print("Data serialization and exiting")
            with open("profile_database.json", "w") as file:
                json.dump(students, file, indent=4)
                print("Serialization completed")
            break
        case _:
            print("Invalid input or invalid operation")