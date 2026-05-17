# =====================================================================
# STRING CONCATENATION (JOINING STRINGS)
# =====================================================================
# Concatenation means gluing multiple strings together end-to-end.
# In Python, we use the plus (+) operator to achieve this.

first_word = "Python"
second_word = "Programming"

# 1. THE BASIC JOIN
# The + operator does NOT automatically add spaces!
joined_broken = first_word + second_word      # Results in: "PythonProgramming"
joined_correct = first_word + " " + second_word  # Adds a literal space string

print("--- Basic Concatenation ---")
print(joined_broken)
print(joined_correct, "\n")


# 2. THE TYPE LIMITATION TRAP
# You can ONLY concatenate strings with other strings. 
rank = 1

# UNCOMMENTING THE LINE BELOW WILL CRASH THE PROGRAM (TypeError):
# print("We are number " + rank) 
# You have to explicitly cast the number to a string first:
print("Fixed Join: We are number " + str(rank) + "!\n")


# =====================================================================
# CONCATENATION VS. F-STRINGS 
# =====================================================================
# Look at how messy it gets when building a full sentence using (+):
name = "John Cena"
city = "Europa"

old_way = "My name is " + name + " and I live in " + city + "."
new_way = f"My name is {name} and I live in {city}."

print("--- The Cleanliness Test ---")
print("Plus Sign Way: ", old_way)
print("f-String Way:  ", new_way)