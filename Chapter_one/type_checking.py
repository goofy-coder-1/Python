# =====================================================================
# PROVING DATA TYPES: THE TYPE() FUNCTION
# =====================================================================
# Python hides data types behind the scenes. To inspect the true identity
# of any variable, we wrap it inside the built-in type() function.

age = 19
item_price = 5.6
character_name = "John Cena"
is_nepal_in_asia = True

# We must wrap type() inside a print() statement to see the output in the terminal!
print("1. Integer Type:  ", type(age))               # Outputs: <class 'int'>
print("2. Float Type:    ", type(item_price))        # Outputs: <class 'float'>
print("3. String Type:   ", type(character_name))    # Outputs: <class 'str'>
print("4. Boolean Type:  ", type(is_nepal_in_asia))   # Outputs: <class 'bool'>


# the terminal prints <class 'int'> instead of just 'int'. 
# In Python, everything is an "object" built from a master blueprint called a "class".