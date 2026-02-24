# Number System Functions Program

def factorial(n):
    if n < 0:
        return "Not defined"
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n <= 0:
        return "Invalid"
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b


def sum_of_digits(n):
    s = 0
    n = abs(n)
    while n > 0:
        s = s + (n % 10)
        n = n // 10
    return s


def reverse_number(n):
    r = 0
    sign = 1
    if n < 0:
        sign = -1
        n = -n

    while n > 0:
        r = r * 10 + (n % 10)
        n = n // 10
    return r * sign


def is_armstrong(n):
    temp = n
    s = 0
    p = len(str(n))

    while temp > 0:
        d = temp % 10
        s = s + (d ** p)
        temp = temp // 10

    return s == n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def is_perfect_number(n):
    if n <= 0:
        return False

    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s == n


def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif ch == 2:
            n = int(input("Enter number: "))
            if is_prime(n):
                print("Prime number")
            else:
                print("Not a prime number")

        elif ch == 3:
            n = int(input("Enter term number: "))
            print("Fibonacci:", fibonacci(n))

        elif ch == 4:
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif ch == 5:
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif ch == 6:
            n = int(input("Enter number: "))
            if is_armstrong(n):
                print("Armstrong number")
            else:
                print("Not an Armstrong number")

        elif ch == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif ch == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif ch == 9:
            n = int(input("Enter number: "))
            if is_perfect_number(n):
                print("Perfect number")
            else:
                print("Not a perfect number")

        elif ch == 10:
            print("Exiting program")
            break

        else:
            print("Invalid choice")


math_menu()