# =====================================================================
# MATH WITH USER INPUT
# =====================================================================
# This script combines input() and type casting to perform real-time 
# calculations based on what the user types.

# 1. Gathering inputs and instantly casting them to the correct math type
price = float(input("Enter item price (Rs.): "))  # Uses float for decimals
quantity = int(input("Enter quantity: "))         # Uses int for whole numbers

# 2. Performing the calculation
total_bill = price * quantity

# 3. Outputting the result using an f-string
print(f"Your total bill comes to: Rs. {total_bill}")