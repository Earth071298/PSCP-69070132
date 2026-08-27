"""ATM"""

def main():
    """ATM"""
    money = int(input())
    notes = [1000,500,100]

    if 100 >= money >= 20000 or money % 100:
        print("ERROR")
    else:
        for i in notes:
            count = money // i
            if count > 0:
                print(i, "=", count)
            money %= i

main()
