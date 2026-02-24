# Number Guessing Game

import random

best = None  # to store best score

while True:
    num = random.randint(1, 100)
    t = 7
    u = 0

    print("\nI have picked a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    while t > 0:
        g = int(input("\nEnter your guess: "))
        u = u + 1
        t = t - 1

        if g == num:
            print("Correct! You guessed the number.")
            print("Attempts used:", u)

            if best is None or u < best:
                best = u
                print("New best score!\n")

            break

        elif g > num:
            print("Too high!")
        else:
            print("Too low!")

        # bonus hint (within 5)
        if abs(g - num) <= 5:
            print("Hint: You are very close!")

        print("Attempts remaining:", t)

    else:
        print("You failed!")
        print("The number was:", num)

    # show best score
    if best is not None:
        print("Best score (minimum attempts):", best)

    ch = input("\nDo you want to play again? (yes/no): ").lower()
    if ch != "yes":
        print("\nThanks for playing!")
        break