"""find unit digit from 7 ** input number"""

number = int(input())

ans = number % 4

if ans == 1 :
    print("7")
elif ans == 2:
    print(9)
elif ans == 3:
    print(3)
else:
    print(1)
