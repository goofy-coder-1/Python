# =============================================================
#                        F O R   L O O P S
# =============================================================

# 1. Looping through a List
# The loop variable ('bike') automatically updates to hold the next item on every pass.
bikes = ["Classic 350", "Interceptor 650", "Himalayan"]

print("--- Iterating through a List ---")
for bike in bikes:
    print(f"Bike profile: {bike}")


# 2. Using range() to repeat an action
# range(5) generates numbers from 0 up to (but not including) 5.
print("\n--- Iterating through a Range ---")
for index in range(5):
    print(f"Loop execution number: {index}")


# 3. Looping through a Dictionary
# We use .items() to pull both the key and the value out at the same time.
user_profile = {
    "username": "goofy-coder-1", 
    "role": "Developer"
}

print("\n--- Iterating through a Dictionary ---")
for key, value in user_profile.items():
    print(f"Key: {key}  Value: {value}")