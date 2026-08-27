"""Bubble Tea"""

def main():
    """Cal"""
    pearl, amount = input().split()
    tea, level, volume = input().split()

    amount = float(amount)
    level = int(level)
    volume = float(volume)

    if pearl == "H":
        pearl_rate = 5
    elif pearl == "O":
        pearl_rate = 3
    else:
        pearl_rate = 2

    if tea == "R":
        tea_rate = [0, 12, 18, 25]
    elif tea == "T":
        tea_rate = [0, 15, 20, 30]
    else:
        tea_rate = [0, 10, 15, 20]

    pearl_cal = amount * pearl_rate
    tea_cal = volume * tea_rate[level]

    total = pearl_cal + tea_cal

    print(f"{total:g}")

main()
