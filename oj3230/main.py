"""hotel room number"""


def main():
    """decode"""
    n = input()
    digits = list(map(int, n))

    floors = [9, 10, 11, 12, 14]
    first = 13

    for digit, floor in zip(digits, floors):
        if digit > 5:
            first = floor
            break

    if n == n[::-1]:
        second = 1 if digits[0] + digits[4] > 5 else 2
        if digits[0] + digits[4] <= 5 and digits[1] * digits[3] <= 5:
            second = 0
    else:
        second = 1 if digits[4] and digits[0] // digits[4] > 5 else 2
        if not (digits[4] and digits[0] // digits[4] > 5) and digits[1] - digits[4] <= 5:
            second = 0

    total = sum(digits)
    product = 1
    for digit in digits:
        product *= digit

    third = 1 if total > 25 else 2 if product > 55 else 0

    print(str(first) + str(second) + str(third))

main()
