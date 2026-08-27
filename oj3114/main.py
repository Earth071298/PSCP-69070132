"""parking"""

def main():
    """Cal"""
    enter_hour, enter_min = map(int, input().split("."))
    leave_hour, leave_min = map(int, input().split("."))

    if not (0 <= enter_hour <= 23 and 0 <= enter_min <= 59):
        print("ERROR")
        return

    if not (0 <= leave_hour <= 23 and 0 <= leave_min <= 59):
        print("ERROR")
        return

    enter_time = enter_hour * 60 + enter_min
    leave_time = leave_hour * 60 + leave_min
    parking_time = leave_time - enter_time

    if parking_time < 0 or parking_time > 1440:
        print("ERROR")
    elif parking_time <= 15:
        print("FREE")
    else:
        hours = (parking_time + 59) // 60

        if hours == 1:
            price = 25
        elif hours == 2:
            price = 50
        elif hours == 3:
            price = 80
        elif hours == 4:
            price = 110
        elif hours == 5:
            price = 145
        elif hours == 6:
            price = 180
        else:
            price = 250

        print(price)

main()
