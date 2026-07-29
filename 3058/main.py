"""membrickmentarity"""

small = int(input())
big = int(input())
goal = int(input())

big_use = min(big, goal // 5)
total = goal - big_use * 5

if total <= small:
    print(total)
else:
    print(-1)
