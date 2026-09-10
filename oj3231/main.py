"""Dice-guessing game"""

def main():
    """check"""
    guess = int(input())
    result = int(input())

    if not (1 <= guess <= 6 and 1 <= result <= 6):
        print("Invalid")
    elif guess == result:
        print("Correct!")
    else:
        print("Wrong!")

main()
