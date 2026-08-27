"""The number in the range [A,B] that leaves a remainder of r when divided by d"""

def main():
    """The number in the range [A,B] that leaves a remainder of r when divided by d"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())

    count = 0

    for x in range(a, b + 1):
        if x % d == r:
            count += 1

    print(count)

main()
