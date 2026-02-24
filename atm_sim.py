# ATM Simulator with Transaction History

bal = 10000          # initial balance
hist = []            # to store transaction history

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Current balance: ₹", bal)
        hist.append("Checked balance: ₹" + str(bal))

    elif ch == 2:
        amt = int(input("Enter amount to deposit: "))
        bal = bal + amt
        print("Deposit successful!")
        print("Updated balance: ₹", bal)
        hist.append("Deposited: ₹" + str(amt))

    elif ch == 3:
        print("Current balance: ₹", bal)
        amt = int(input("Enter amount to withdraw: "))

        if amt > bal:
            print("Transaction failed: Insufficient balance!")
            hist.append("Failed withdrawal of: ₹" + str(amt))

        elif bal - amt < 500:
            print("Transaction failed: Minimum balance of ₹500 must be maintained!")
            hist.append("Failed withdrawal (min balance rule) ₹" + str(amt))

        else:
            bal = bal - amt
            print("Withdrawal successful!")
            print("Updated balance: ₹", bal)
            hist.append("Withdrawn: ₹" + str(amt))

    elif ch == 4:
        print("=== TRANSACTION HISTORY ===")
        if len(hist) == 0:
            print("No transactions yet")
        else:
            for h in hist:
                print("-", h)

    elif ch == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")