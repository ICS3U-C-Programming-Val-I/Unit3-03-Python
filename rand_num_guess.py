#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 16, 2023
# This program chooses a random number then asks the user to
# guess it, then it lets them know if they are right.

import random


def main():
    # input - get guess from user.
    user_guess = int(input("Pick a number between 0 and 9\n"))

    # process - set correct answer and check guess.
    correct_answer = random.randint(0, 9)
    if correct_answer == user_guess:
        # output - display result
        print("Correct, you got it right.")
    else:
        # output - display result
        print(f"Incorrect, the correct number is {correct_answer}")


if __name__ == "__main__":
    main()
