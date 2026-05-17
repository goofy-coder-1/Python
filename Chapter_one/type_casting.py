# =====================================================================
# TYPE CASTING (DATA CONVERSION)
# =====================================================================
# Type casting is the process of converting a variable from one data 
# type to another. In Python, we use built-in constructor functions.

# --- 1. STRING TO NUMBERS (Crucial for User Inputs) ---
string_num = "100"
string_decimal = "45.75"

# Converting text into math-ready integers and floats
converted_int = int(string_num)        # "100" becomes 100
converted_float = float(string_decimal)  # "45.75" becomes 45.75

print("--- String to Numbers ---")
print(f"Integer Math: {converted_int + 50}")      # Outputs: 150
print(f"Float Math:   {converted_float * 2}\n")    # Outputs: 91.5


# --- 2. NUMBERS TO STRINGS (For Text Manipulation) ---
integer_age = 20
float_gpa = 3.8

# Converting numbers into text characters
string_age = str(integer_age)  # 20 becomes "20"
string_gpa = str(float_gpa)    # 3.8 becomes "3.8"

print("--- Numbers to Strings ---")
print("My age as text: " + string_age)
print(f"Data Type now:  {type(string_gpa)}\n")  # <class 'str'>


# --- 3. FLOAT TO INT (The Truncation Trap) ---
# Warning: Converting a float to an int does NOT round up or down.
# It completely chops off (truncates) the decimal part!
pi_value = 3.9999
chopped_pi = int(pi_value)  # Becomes exactly 3, losing all decimals

print("--- Float to Integer Danger ---")
print(f"Original Float: {pi_value}")
print(f"Chopped Integer: {chopped_pi}\n")  # Outputs: 3


# --- 4. CRASH TRAP (Invalid Casts) ---
# You can only convert strings that look like pure numbers!
corrupt_data = "123abc"

# UNCOMMENTING THE LINE BELOW WILL CRASH THE PROGRAM (ValueError):
# broken_cast = int(corrupt_data) 
# Python cannot extract numbers from raw words.