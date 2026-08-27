"""Bonus"""

def bonus_cal():
    """cal"""
    position, year,s = input().split()
    year = int(year)
    s = int(s)
    bonus = 0

    if position == "M":
        if year <= 5:
            bonus = 1500 + s * 0.06
        elif year <= 10:
            bonus = 1500 + s * 0.08
        else:
            bonus = 1500 + s * 0.10

    elif position == "B":
        if year <= 5:
            bonus = 1000 + s * 0.05
        elif year <= 10:
            bonus = 1000 + s * 0.06
        else:
            bonus = 1000 + s * 0.07

    elif position == "G":
        if year <= 5:
            bonus = 500 + s * 0.04
        elif year <= 10:
            bonus = 500 + s * 0.05
        else:
            bonus = 500 + s * 0.06

    print(int(bonus))

bonus_cal()
