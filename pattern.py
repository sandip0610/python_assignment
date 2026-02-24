# Pattern Printing Program

p = int(input("Choose pattern (1-7): "))


# Pattern 1
if p == 1:
    h = int(input("Enter height: "))
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2
elif p == 2:
    h = int(input("Enter height: "))
    for i in range(1, h + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3
elif p == 3:
    h = int(input("Enter height: "))
    for i in range(h, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
elif p == 4:
    h = int(input("Enter height: "))
    for i in range(1, h + 1):
        for j in range(i,h+1):
            print(" ",end="")
        # increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

#right aligned
elif p==5:
    h = int(input("Enter height: "))
    for i in range(1, h + 1):
        for j in range(i,h+1):
            print(" ",end="")
        for j in range(1, i + 1):
            print(j, end="")
        print()

elif p == 6:
    h = int(input("Enter height: "))
    for i in range(h, 0, -1):
        for j in range(i,h+1):
            print(" ",end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()
# Hollow Square Pattern
elif p==7:


    n = int(input("Enter size: "))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

else:
    print("Invalid pattern choice")