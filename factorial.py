# Factorial calculation using loop
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("0! = 1")
else:
    f = 1
    print(str(n) + "! =", end=" ")

    for i in range(n, 0, -1):
        f = f * i
        print(i, end="")
        if i != 1:
            print(" × ", end="")

    print(" =", f)