# Palindrome Checker Program

x = input("Enter a word or number: ")
# convert to string and handle case
s = str(x)
s2 = s.lower()
s2=s2.replace(" ","")

rev = ""
n = len(s2)

print("Step-by-step check:")
# reverse using loop
for i in range(n):
    rev =  s2[i]+rev
    print("Reversed till now:", rev)

print("Original:", s2)
print("Reversed:", rev)

# check palindrome
if s2 == rev:
    print("Result:", x, "is a Palindrome")
else:
    print("Result:", x, "is NOT a Palindrome")