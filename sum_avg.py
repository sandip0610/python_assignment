n=int(input("Enter how many number you want: "))
s=0
for i in range(n):
    e=int(input(f"enter number {i+1}: "))
    s+=e
    if i==0:
        m,mi=e,e
    else:
        if e>m:
            m=e
        if e<mi:
            mi=e
print(f"Sum: {s}")
print(f"Average: {(s/n):.2f}")
print(f"Maximum Number: {m}")

print(f"Minimum Number: {mi}")