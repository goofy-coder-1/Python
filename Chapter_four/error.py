# ==============================================================================
# CHAPTER 5: EXCEPTION HANDLING & DEFENSIVE CODING
# ==============================================================================

# If a user inputs 0 here, the program normally dies instantly with a ZeroDivisionError
# If a user inputs 'abc', it dies with a ValueError

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print(f"Result: {result}\n")

except ValueError:
    # Captures inputs that can't be converted to integers (like strings or symbols)
    print("Input Error: You must enter whole numbers only! Letters and symbols are not allowed.\n")

except ZeroDivisionError:
    # Captures the ultimate math sin: dividing by zero
    print("Math Error: You cannot divide a number by zero! The universe would collapse.\n")


print("---  File Handling Safety Net ---")
# Let's try to open a file that doesn't exist yet

try:
    with open("missing_database.json", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    # Instead of crashing your project, we catch the error and handle it cleanly
    print("File status: 'missing_database.json' was not found on disk.")
    print("System Action: Initializing a fresh configuration profile automatically...")
    
    with open("missing_database.json", "w") as file:
        file.write('{"status": "initialized", "attempts": 1}')
    print("Fresh database footprint deployed smoothly.\n")
