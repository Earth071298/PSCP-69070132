"""Tuple's Sad life"""

def main():
    """Tuple's Sad life"""
    values = tuple(input().split())
    target = input().strip()

    position = values.index(target)
    amount = values.count(target)

    for _ in range(amount):
        print(" ".join([str(position)] * amount))

main()
