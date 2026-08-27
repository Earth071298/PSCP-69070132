"""Calculate the estimated taxi fare"""

def main():
    """Calculate the estimated taxi fare"""
    distance = int(input())
    price = 35

    if distance == 1:
        price = 35
    elif distance <= 0:
        price = 0
    elif distance <= 10:
        price += (distance - 1) * 5
    else:
        price += 45 + ((distance - 10) * 8)
    print(price)

main()
