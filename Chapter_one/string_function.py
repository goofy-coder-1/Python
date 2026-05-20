# =============================================================
#           S T R I N G   F U N C T I O N S
# =============================================================

# 1. String Slicing
# Slicing lets us extract a specific range of characters using [start:end].
# Python stops right BEFORE the 'end' index.
txt = "Hello, How are you?"
print("--- String Slicing ---")
print("Slice [2:5]:", txt[2:5])   # Outputs: llo
print("Slice [:5]: ", txt[:5])    # Start to index 5: Hello
print("Slice [2:]: ", txt[2:])    # Index 2 to the very end: llo, How are you?

# 2. Case Modifications
print("\n--- Case Modifications ---")
print("Upper:", txt.upper())      # Converts all characters to uppercase
print("Lower:", txt.lower())      # Converts all characters to lowercase
print("Title:", txt.title())      # Capitalizes first letter of every word

sentence = "hello world"
print("Capitalize:", sentence.capitalize())  # Capitalizes ONLY the initial character of the string

# 3. Stripping and Cleaning
print("\n--- Stripping Whitespace ---")
spaced_txt = "   Hello World   "
# .strip() removes extra spaces *only* from the beginning and end of a string
print(f"Original: '{spaced_txt}'")
print(f"Cleaned:  '{spaced_txt.strip()}'")

# 4. Modifying and Splitting
print("\n--- Replace and Split ---")
# .replace() is case-sensitive. It targets specific targets to switch them out.
print("Replaced:", txt.replace("H", "Me")) 

# .split() without arguments cuts strings at every whitespace gap and creates a List
words_list = txt.split()
print("Split into List:", words_list) # Note: The comma stays attached to 'Hello,'

# 5. Type and Verification Checks
print("\n--- Verification Checks ---")
# .isalpha() returns True ONLY if the string contains pure alphabetic letters (A-Z) with no spaces/symbols
print(f"Is '{sentence}' pure alpha?", sentence.isalpha()) # False, because it counts the space character

numeric_str = "2026"
print(f"Is '{numeric_str}' pure numbers?", numeric_str.isdigit()) # True

# Removing ALL Spaces inside a sentence
# Unlike .strip() which only cleans the outer edges, .replace(" ", "") squeezes out everything.
spaced_sentence = "H e l l o   W o r l d"
no_spaces = spaced_sentence.replace(" ", "")

print("\n--- Removing All Internal Spaces ---")
print("Original spaced sentence:", spaced_sentence)
print("Squeezed sentence:      :", no_spaces) # Outputs: HelloWorld

# These are some of the basic string function that you might use on initial phases but as you dive deeper,
# you will learn about other methods as well
# I highly recommend you to explore sites like 'official python documentation' 'w3schools' 'freecodecamp' for good understanding on these
