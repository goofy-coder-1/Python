# =====================================================================
# CAPTURING USER INPUT
# =====================================================================
# The input() function stops your program and waits for the user to type.
# CRITICAL NOTE: input() ALWAYS captures data as a String (text) by default!

# 1. Standard Text Input
visitor_name = input("Enter your name: ")
print(f"Welcome to the terminal, {visitor_name}!")


raw_birth_year = input("Enter your birth year: ")

print(f"Data type of your input: {type(raw_birth_year)}") 
# Even if you typed 2006, this outputs: <class 'str'>

# This line would crash because you cannot subtract a string from an int:
# current_age = 2026 - raw_birth_year  


# Explicitly wrap input() inside int() to force it into a math-ready number.
converted_birth_year = int(input("Enter your birth year again to fix the bug: "))

print(f"New data type after casting: {type(converted_birth_year)}")
# This successfully outputs: <class 'int'>

current_age = 2026 - converted_birth_year  # Math works now!
print(f"You are {current_age} years old.")