# Program to calculate age details

# taking birth year from user
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year

print("Current Age:", age)

# age calculations
print("Age in months:", age * 12)
print("Age in days:", age * 365)
print("Age in hours:", age * 365 * 24)
print("Age in minutes:", age * 365 * 24 * 60)

# years left to reach 100
print("Years until age 100:", 100 - age)