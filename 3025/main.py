"""Season"""

month = int(input())
date = int(input())

if (month <= 2) or (month == 3 and date < 21) or (month == 12 and date >= 21):
    print("winter")
elif (month == 3 and date >= 21) or (4 <= month <= 5) or (month == 6 and date < 21):
    print("spring")
elif (month == 6 and date >= 21) or (7 <= month <= 8) or (month == 9 and date < 21):
    print("summer")
elif (month == 9 and date >= 21) or (10 <= month <= 11) or (month == 12 and date < 21):
    print("fall")
