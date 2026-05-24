# ==============================================================================
# MODULE: bmibox.py
# ==============================================================================

def calculate_metabolism(weight, height, age):
    # Loop until we secure a pristine validation on Gender
    while True:
        gender = input("Gender ('M' for male / 'F' for female): ").lower().strip()
        if gender in ['m', 'f']:
            break
        print("[-] Selection Error: Please enter exactly 'M' or 'F'.")

    # Execute Mifflin-St Jeor Formula
    match gender:
        case 'm':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        case 'f':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            
    print(f"\nYour Base Metabolic Rate (BMR): {bmr:.2f} kcal/day")
    
    # Activity Multiplier Menu
    print("\n--- Select Your Daily Activity Level ---")
    print("[1] Sedentary (Desk job, minimal activity)")
    print("[2] Lightly Active (Light exercise 1-3 days/week)")
    print("[3] Moderately Active (Moderate training 3-5 days/week)")
    print("[4] Very Active (Heavy lifting/sports 6-7 days/week)")

    while True:
        try:
            choice = int(input("Enter choice (1-4): "))
            match choice:
                case 1: 
                    multiplier = 1.2
                    break
                case 2:
                    multiplier = 1.375
                    break
                case 3:
                    multiplier = 1.55
                    break
                case 4:
                    multiplier = 1.725
                    break
                case _:
                    print("[-] Index Out of Bounds: Select a digit between 1 and 4.")
        except ValueError:
             print("[-] Input Error: Enter a raw single digit.")

    # Compute Final Total Daily Energy Expenditure
    tdee = bmr * multiplier

    # Print out the Comprehensive Fitness Report Matrix
    print("\n=============================================")
    print("         TITAN FITNESS MATRIX ENGINES        ")
    print("=============================================")
    print(f"Maintenance Energy:    {tdee:.0f} kcal/day")
    print(f"Titan Shred (-500):    {tdee - 500:.0f} kcal/day (Fat Loss)")
    print(f"Titan Bulk (+500):     {tdee + 500:.0f} kcal/day (Muscle Gain)")
    print("=============================================\n")
         
