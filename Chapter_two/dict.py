# =============================================================
#                D I C T I O N A R I E S 
# =============================================================

# 1. Creating a Dictionary
# Dictionaries use curly braces {}. Keys must be unique, values can be anything.
user_profile = {
    "username": "goofy-coder-1",
    "role": "Developer",
    "status": "Active"
}
print("Original dictionary:", user_profile)

# 2. Accessing Values
# You look up a value by passing its key inside square brackets.
current_role = user_profile["role"]
print(f"User Role: {current_role}")

# 3. Modifying and Adding Key-Value Pairs
# If the key exists, it updates the value. If it doesn't exist, it creates a new one.
user_profile["status"] = "Coding"  # Updating existing key
user_profile["language"] = "Python"  # Adding a completely new key
print("Updated dictionary:", user_profile)

# 4. Checking if a Key Exists
# You can use the 'in' keyword to check for a key before looking it up.
has_score = "sat_score" in user_profile
print("Is sat_score in the profile?", has_score)