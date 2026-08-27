"""Express Delivery"""

def main():
    """Calculate delivery fee."""
    start, end = input().split()
    weight = float(input())

    if start == "BKK" and end == "CNX":
        fee = 10 + weight * 30
    elif start == "CNX" and end == "UBP":
        fee = 15 + weight * 40
    elif start == "UBP" and end == "BKK":
        fee = 20 + weight * 40
    elif start == "BKK" and end == "PKT":
        fee = 25 + weight * 50
    elif start == "PKT" and end == "CNX":
        fee = 30 + weight * 60
    elif start == "UBP" and end == "PKT":
        fee = 40 + weight * 70
    else:
        print("Error")
        return

    print(f"{fee:.2f}")

main()
