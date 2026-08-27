"""Gift"""

def gift():
    """giftcal"""
    radius, height, glue = map(float, input().split())

    width = (2 * radius) + height
    length = 2 * 3.14 * radius + glue

    print(f"{width:.2f} {length:.2f}")

gift()
