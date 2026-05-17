## =====================================================================
# TYPES OF DATA USED IN PROGRAMMING
# =====================================================================

# 1. Integer: Whole numbers (positive or negative) without decimals.
integer_number = 9  

# 2. Float: Fractional, floating-point numbers containing a decimal point.
float_number = 5.6   

# 3. Character: Python treats a single letter as a string of length 1.
single_character = "P" 

# 4. String: A sequence or formation of multiple characters chained together.
text_string = "Hello What's up" 

# Displaying all four core data types in the terminal at once
print("Core Data Types:", integer_number, float_number, single_character, text_string)


# =====================================================================
# METHODS OF USING VARIABLES IN OUTPUT (PRACTICAL EXAMPLES)
# =====================================================================
name = "John Cena"

# Method A: Using an f-string (Modern, clean, and highly recommended)
# It injects variables directly into the text layout inside curly braces.
print(f"I am really glad that I met you Mr. {name}. Is your day going good? Heard you had {integer_number} beers!")

# Method B: Using Comma Separation (Traditional approach)
# commas automatically add spaces and split your sentence so you need few other lines of code to prevent that.
print("I am really glad that I met you Mr.", name)
print("Heard you had", integer_number, "beers!")


# =====================================================================
# ADVANCED COLLECTIONS & LOGIC
# =====================================================================
# There are also structures like Booleans, Lists, and Dictionaries. 
# While they act as data classifications, they serve unique structural roles 
# and are documented in their own dedicated files within this folder.