# Taking inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")
college = input("Enter your college: ")
email = input("Enter your email: ")

# Display formatted bio card
print("\n" + "=" * 40)
print("         STUDENT BIO CARD")
print("=" * 40)
print(f"Name     : {name}")
print(f"Age      : {age} years")
print(f"Course   : {course}")
print(f"College  : {college}")
print(f"Email    : {email}")
print("=" * 40)
