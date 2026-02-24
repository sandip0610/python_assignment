# Simple Calculator using Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def dvd(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b
def perc(a, b):
    if b == 0:
        return "Error: Total cannot be zero"
    return (a / b) * 100
def sqr(a):
    if a < 0:
        return "Error: Square root of negative number"
    return a ** 0.5

def calculator():
    while True:
        print("\nCALCULATOR")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Percentage")
        print("8. Square Root")
        print("9. Exit")

        ch = int(input("Enter choice: "))

        if ch == 9:
            print("Exiting calculator")
            break

        if ch == 8:
            a = float(input("Enter number: "))
            print("Square root:", sqr(a))
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if ch == 1:
            print("Result:", add(a, b))
        elif ch == 2:
            print("Result:", sub(a, b))
        elif ch == 3:
            print("Result:", mul(a, b))
        elif ch == 4:
            print("Result:", dvd(a, b))
        elif ch == 5:
            print("Result:", mod(a, b))
        elif ch == 6:
            print("Result:", power(a, b))
        elif ch==7:
            print(f"Result: {perc(a,b)}%")
        else:
            print("Invalid choice")

# calling main function
calculator()