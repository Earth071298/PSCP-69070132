"""Big Sale"""

def main():
    """Big Sale"""
    a, b, c = map(int, input().split())

    total = a * 25 + b * 40 + c * 55
    count = a + b + c

    if count >= 3:
        total = int(total * 0.90)

    print(total)

main()
