# ====================================================
#              K W A R G S
# ====================================================

# Using **kwargs (Unlimited Keyword Arguments)
# The double asterisk '**' tells Python to grab ALL named pairs (key=value)
# and pack them neatly into a single Dictionary named 'details'.

# Example first
def playerStats(**details):
    print("\n--- Processing Player Profile ---")
    # Because 'details' is a dictionary, we can use .items() to loop through it
    for key, value in details.items():
        # .title() cleans up the keys dynamically for display
        print(f"{key.title()}: {value}")

# We pass named values directly into the function call
playerStats(name="Julius Caesar", rank="Gold", character="Duelist", level="45")
playerStats(name="Alexander", rank="Diamond", ping="45ms")


# Example second
def totalCost(item_name, **taxes):
    base_price = 100
    total = base_price
    
    print(f"\n======= Bill for {item_name} =======")
    print(f"Base Price: ${base_price}")
    
    for tax_name, amount in taxes.items():
        print(f"+ {tax_name.title()}: ${amount}")
        total += amount
        
    return f"Final Total: ${total}"

# Different regions might have completely different tax configurations
print(totalCost("Custom Exhaust", vat=13, luxury_tax=20, shipping=5))
print(totalCost("Stock Mirror", vat=13))