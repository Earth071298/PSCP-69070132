"""triengel"""

def main():
    """tri"""

    num = int(input())

    if num < 4:
        for i in range(1,num+1):
            print("0" * i)
    else:
        print("0")
        print("00")
        for i in range(1,num-2):
            print("0" + "1" * i + "0")
        print("0" * num)

main()
