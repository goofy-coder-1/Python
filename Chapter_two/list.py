# =============================================================
#                        L I S T S 
# =============================================================

# 1. Creating a List
# A list holds an ordered collection of items, which can be changed (mutable).
bikes = ["Classic 350", "Duke 390", "Himalayan"]
print("Original list:", bikes)

# 2. Accessing Items (Indexing)
# Python starts counting at 0. Negative indexing starts from the end (-1).
first_bike = bikes[0]
last_bike = bikes[-1]
print(f"First bike: {first_bike} | Last bike: {last_bike}")

# 3. Modifying an Item
# You can change any item by targeting its index.
bikes[1] = "Interceptor 650"
print("After modifying index 1:", bikes)

# 4. Adding Items
# Use .append() to add an item to the very end of the list.
# There will be a seperate file that will help you understand string functions very well, but append is all for now
bikes.append("R15")
print("After appending a new bike:", bikes)

# 5. Getting List Length
# The len() function tells you how many items are in the list.
print("Total number of bikes:", len(bikes))


