# ==============================================
#        F U N C T I O N
# ==============================================

# A function is a reusable block of code that only runs when called.
# We define them using 'def', pass data via 'arguments', and send data back via 'return'.

# 1. A Simple Function (No inputs, no outputs)
def greet_user():
    print("Welcome to Chapter Three, Developer!")

print("--- Calling a Simple Function ---")
greet_user()  # This executes the code block inside the function

# 2. Function with Parameters (Passing data inside)
# 'username' is a parameter—a placeholder for incoming data.
def user_greeting(username):
    if username == "Kaido":
          print(f"Welcome, master {username}")
    else:
         print(f"Welcome {username}")

name = input("Enter your name: ")
user_greeting(name)