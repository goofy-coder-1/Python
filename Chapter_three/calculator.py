# ====================================================
# BASIC CALCULATOR USING FUNCTION AND MATCH CASE
# ====================================================

def addFunction(a, b):
    return a + b

def subFunction(a, b):
    return a - b

def mulFunction(a, b):
    return a * b

def divFunction(a, b):
    return a / b

def main():
    print("--- Functional Calculator Active ---")
    
    # Using float() handles decimals and whole numbers without crashing
    a = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))

    match operation:
        case '+':
            print(f"Result: {addFunction(a, b)}")
        case '-':
            print(f"Result: {subFunction(a, b)}")
        case '*':
            print(f"Result: {mulFunction(a, b)}")
        case '/':
            if b == 0:
                print("Error: Invalid denominator (Division by Zero)")
            else:
                print(f"Result: {divFunction(a, b)}")
        case _:
            print("Error: Invalid operation")


if __name__ == "__main__":
    main()