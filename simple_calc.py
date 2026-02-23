# Program to perform basic arithmetic operations

# taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Results:")

# addition
print(num1, "+", num2, "=", num1 + num2)
# subtraction
print(num1, "-", num2, "=", num1 - num2)
# multiplication
print(num1, "*", num2, "=", num1 * num2)
# division (rounded to 2 decimal places)
print(num1, "/", num2, "=", round(num1 / num2, 2))
# modulus
print(num1, "%", num2, "=", num1 % num2)
# exponentiation
print(num1, "^", num2, "=", num1 ** num2)