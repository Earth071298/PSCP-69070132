"""Inflation"""

def main():
    """calculate"""
    price = input()
    years = int(input())

    if "." in price:
        whole, decimal = price.split(".")
        decimal = (decimal + "00")[:2]
    else:
        whole = price
        decimal = "00"

    price = int(whole) * 100 + int(decimal)

    for _ in range(years):
        increase = price * 381 // 10000
        price += increase

    print(f"{price // 100}.{price % 100:02d}")

main()
