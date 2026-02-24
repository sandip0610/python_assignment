# Multiplication table for a given number
n = int(input("Enter number: "))
r = int(input("Enter range (end): "))

print("Multiplication Table of", n)

for i in range(1, r + 1):
    print(n, "x", i, "=", n * i)

# Full multiplication table (1 to 10)

print("FULL MULTIPLICATION TABLE (1 to 10)\n")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j} = ",i * j, end="\t")
    print()