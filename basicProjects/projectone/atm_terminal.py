# =====================================
#             A T M
# =====================================

from basicProjects.projectone.atmbox import atmBox

realpassword = "567484"
attempts = 3

# Loop runs as long as the user has attempts left
while attempts > 0:
    try:
        # Keeping it as a string to match 'realpassword'
        pass_word = input("Enter password: ")
        
        if realpassword == pass_word:
            print("\n--- Access Granted ---")
            atmBox()  # Call the function with parentheses
            break     # Exit the loop after a successful transaction
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts remaining: {attempts}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if attempts == 0:
    print("Account locked. Too many incorrect attempts.")

