# =====================================================================
# DAY 1: Dynamic Typing, Inputs, and Type Casting
# =====================================================================

# 1. Inputs always come in as STRINGS by default in Python
raw_gpa = input("Enter your target GPA for RJU Semester 2: ")
print(f"Initial type of input: {type(raw_gpa)}") 

# 2. Type Casting (Converting data types)
# We can't do math on a string, so we force it into a Float
clean_gpa = float(raw_gpa)
print(f"Converted type: {type(clean_gpa)}")

# 3. Dynamic Calculation
# Adding a 0.15 cushion to your 3.70 goal to ensure safety
safety_buffer = clean_gpa + 0.15

# 4. Clean formatting using f-strings
# The ':.2f' inside the curly braces forces it to display only 2 decimal places
print("\n--- TARGET UPDATE ---")
print(f"Targeting an elite: {clean_gpa}")
print(f"Daily routine safety threshold: {safety_buffer:.2f}")