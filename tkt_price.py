# Movie Ticket Pricing System

n = int(input("Enter number of tickets: "))
print("Enter Day [Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday]")
d = input("Enter day of week: ").lower()

t = 0  # total amount before discount

for i in range(1, n + 1):
    a = int(input("Enter age of person " + str(i) + ": "))

    if a < 3:
        p = 0
        c = "Free"
    elif a <= 12:
        p = 150
        c = "Child"
    elif a <= 59:
        p = 300
        c = "Adult"
    else:
        p = 200
        c = "Senior"

    print("Person", i, "category:", c, ", Ticket price: ₹", p)
    t = t + p

# discount based on day
if d == "friday" or d == "saturday" or d == "sunday":
    dis = 20
else:
    dis = 0

# final calculation
da = t * dis / 100
fa = t - da

print("=== MOVIE TICKET BILL ===")
print("Base amount: ₹", t)
print("Discount:", dis, "%")
print("Discount amount: ₹", round(da, 2))
print("Price after discount: ₹", round(fa, 2))
print("Total amount to pay: ₹", round(fa, 2))