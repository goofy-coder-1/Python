# ===============================
#     A T M  B O X
# ===============================

def atmBox():
    operation = input("Enter the operation (C: Check, W: Withdraw, D: Deposit): ").upper()
    Base_capital = 8848
    
    match operation:
        case 'C':
            print(f"Current Balance: ${Base_capital}")
        case 'W':
            try:
                withdraw = int(input("Enter the amount to withdraw: "))
                remaining = Base_capital - withdraw
                print(f"Capital withdrawn: ${withdraw}")
                print(f"Remaining Capital: ${remaining}")
                if remaining < 0:
                    # Using abs() to turn a negative number positive for cleaner debt text
                    print(f"You have gone ${abs(remaining)} into debt")
            except ValueError:
                print("Please enter a valid number for withdrawal.")
        case 'D':
            try:
                deposit = int(input("Enter the amount to be deposited: "))
                print(f"Deposited Amount: ${deposit}")
                print(f"Available Capital: ${Base_capital + deposit}")
            except ValueError:
                print("Please enter a valid number to deposit.")
        case _:
            print("Invalid operation selected.")