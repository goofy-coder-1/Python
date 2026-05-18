# =============================================================
#                     W H I L E   L O O P S
# =============================================================

# 1. Basic While Loop
# A while loop repeats a block of code as long as a specified condition is True.
counter = 1
print("--- Counting up to 3 ---")
while counter <= 3:
    print(f"Current count: {counter}")
    counter += 1  # Crucial step: changes the condition so the loop eventually stops

# 2. Breaking out of a Loop Early
# You can use the 'break' statement to instantly exit a loop, even if the condition is still True.
print("\n--- Breaking a loop early ---")
number = 10
while number > 0:
    if number == 7:
        print("Found number 7! Breaking the loop.")
        break
    print(f"Checking number: {number}")
    number -= 1

# 3. Skipping an Iteration
# The 'continue' statement stops the current pass and jumps straight back to the top of the loop.
print("\n--- Skipping an item with continue ---")
skip_counter = 0
while skip_counter < 5:
    skip_counter += 1
    if skip_counter == 3:
        print("Skipping 3!")
        continue
    print(f"Processing number: {skip_counter}")