"""Ticket"""

def main():
    """Ticket"""
    age, day = input().split()
    age = int(age)

    if age < 5:
        price = 0
    elif age <= 18:
        price = 100
    else:
        price = 150

    if day == "Wed":
        price //= 2

    print(price)

main()
