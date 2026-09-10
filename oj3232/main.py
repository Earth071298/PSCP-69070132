"""frog jumps"""

def main():
    """jumps"""
    x, y = map(int, input().split())

    total = 0
    jumps = 0
    distance = x

    while distance > 0 and total < y:
        total += distance
        jumps += 1
        distance -= 2

    if total >= y:
        print(jumps)
    else:
        print(-1)

main()
