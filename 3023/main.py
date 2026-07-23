"""Find the number of button presses"""

num = int(input())
if num == 1 :
    print(1)
else:
    count = 0
    i = 1
    while i <= num:
        x = i
        while x > 0:
            count += 1
            x //= 10
        i += 1
    
    print(count + num)
