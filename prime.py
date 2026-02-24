# Prime number check program
print("Enter your choice")
print("1. To find if a single number is prime or not")
print("2: To find prime numbers between 2 given range")
choice=int(input("Enter choice: "))


def prime_check(n):

    if n < 0:
        return False
    elif n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        is_prime = True

        for i in range(2, n//2+1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            return True
        else:
            return False


if choice==1:
    n = int(input("Enter a number: "))
    if prime_check(n):
        print(n, "is a Prime number")
    else:
        print(n, "is NOT a prime number")
elif choice==2:
    a=int(input("Enter first range: "))
    b=int(input("Enter second range: "))

    print("Prime Numbers: ",end="")
    first = True

    for i in range(a, b + 1):
        if prime_check(i):
            if not first:
                print(",", end="")
            print(i, end="")
            first = False
else:
    print("wrong choice")