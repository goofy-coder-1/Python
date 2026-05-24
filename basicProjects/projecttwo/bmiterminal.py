# ==============================================================================
# ENTRY ENGINE: fitness_engine.py
# ==============================================================================
from bmibox import calculate_metabolism

print("=====================================")
print("     THE TITAN METABOLIC SYSTEM      ")
print("=====================================")

while True:
    # Protect inputs with absolute Chapter 5 Error Armor
    try:
        weight = float(input("Weight (kg): "))
        age = int(input("Age (Years): "))
        height = float(input("Height (cm): "))
        
        # Verify numbers make logical sense before running calculations
        if weight <= 0 or age <= 0 or height <= 0:
            print("[-] Input Error: Physical metrics must be greater than zero.\n")
            continue
            
        # Fire off our calculator engine module
        calculate_metabolism(weight, height, age)
        
        # Fixed break conditional logic loop alignment
        choice = input("Would you like to run another calculation? (Y/N): ").upper().strip()
        if choice != "Y":
            print("\nStay dedicated, Titan. Bye Bye Fam!")
            break
            
    except ValueError:
        print("[-] System Refusal: Invalid data stream detected. Use digits only for metric inputs.\n")