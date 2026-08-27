"""pod"""

n, k = map(int, input().split())

rows = [0] * k
waiting = 0

for _ in range(n):
    row = int(input()) - 1
    rows[row] += 1
    waiting += 1
    if min(rows) > 0:
        for i in range(k):
            rows[i] -= 1
        waiting -= k

print(waiting)
