# =====================================================================
# BOOLEANS (bool)
# =====================================================================
# Booleans are crucial for comparisons, searches, and making decisions.
# They only have two possible values (Note the capital letters!):
# 1. True
# 2. False

is_nepal_in_asia = True
sentence = "Nepal is in Asia:"

print(sentence, is_nepal_in_asia)

# =====================================================================
# PRACTICAL EXAMPLE USING COMPARISON
# =====================================================================
# Let's ask the user for a number to test a logic state

user_number = int(input("Enter a number: ")) 

# We initialize our boolean tracker
is_greater = False 

if user_number > 3:
    is_greater = True
    print("Given number is greater than 3.")
else:
    is_greater = False 
    print("Given number is smaller than or equal to 3.")

# Proving the boolean state changed based on user input
print(f"Is the number greater than 3? State: {is_greater}")
