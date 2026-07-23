"""Coke cap promotion"""

price_coke = int(input())
cap_promotion = int(input())
promotion_price = int(input())
coke = int(input())

bottle = 0
cap = 0
total_price = 0

while bottle < coke:
    if cap >= cap_promotion:
        total_price += promotion_price
        bottle += 1
        cap -= cap_promotion
        cap += 1
    else:
        total_price += price_coke
        bottle += 1
        cap += 1

if cap_promotion == 0:
    print(price_coke * coke)
else:
    print(total_price)
