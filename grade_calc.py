# Program to calculate result and grade

# taking marks for 5 subjects
sub1 = int(input("Enter marks for Subject 1:"))
sub2 = int(input("Enter marks for Subject 2:"))
sub3 = int(input("Enter marks for Subject 3:"))
sub4 = int(input("Enter marks for Subject 4:"))
sub5 = int(input("Enter marks for Subject 5:"))

print("Marks in each subject:")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)

# total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")

# result check
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

# grade calculation
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

print("Grade:", grade)
print("Result:", result)