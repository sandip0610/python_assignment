# Leap Year Checker Program
y = int(input("Enter a year: "))
# checking leap year conditions
if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print(y, "is a Leap Year")
    
    if y % 400 == 0:
        print("Reason: Divisible by 400")
    else:
        print("Reason: Divisible by 4 and not divisible by 100")
else:
    print(y, "is NOT a Leap Year")
    
    if y % 100 == 0:
        print("Reason: Divisible by 100 but not by 400")
    else:
        print("Reason: Not divisible by 4")