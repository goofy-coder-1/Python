# =====================================================================
# NUMERIC OPERATIONS (INTEGERS & FLOATS)
# =====================================================================
# This file covers how Python handles mathematical operations between 
# whole numbers (int) and decimal numbers (float).

num_a = 10  # Type: Integer
num_b = 3   # Type: Integer

# 1. Standard Division (/) ALWAYS returns a Float, even if it divides perfectly!
div_result = num_a / num_b  # Result: 3.3333333333333335
exact_div = 4 / 2           # Result: 2.0 (Still a float!)

# 2. Floor Division (//) truncates the decimal and rounds down to an Integer
floor_result = num_a // num_b  # Result: 3

# 3. Modulus (%) returns the REMAINING remainder of a division
modulo_result = num_a % num_b  # Result: 1 ( 3 goes into 10 three times, with 1 left over)

# 4. Exponentiation (**) is used for calculating powers (instead of ^)
squared_result = num_b ** 2  # Result: 9 (3 to the power of 2)

print("Standard Div:", div_result)
print("Exact Div: ", exact_div)
print("Floor Div:", floor_result)
print("Remainder (Modulo):", modulo_result)
print("Power (Exponent):", squared_result)