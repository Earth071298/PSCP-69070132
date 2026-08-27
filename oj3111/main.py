"""School Cooperative"""

from decimal import Decimal, ROUND_HALF_UP

def discount():
    """cal payment"""
    status = input()
    items = []

    for _ in range(int(input())):
        amount = Decimal(input())
        items.append(amount)

    subtotal = sum(items)

    if status == "Y":
        payment = subtotal * Decimal("0.95")
    elif subtotal >= 500:
        payment = subtotal * Decimal("0.97")
    else:
        payment = subtotal

    payment = payment.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    print(payment)

discount()
