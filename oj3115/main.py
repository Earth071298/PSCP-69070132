"""Arcade of Time"""

def main():
    """Check"""
    num, check = map(int, input().split())

    change = [0] * 1441

    for _ in range(num):
        start, stop = map(int, input().split())
        change[start] += 1
        change[stop] -= 1

    open_store = [0] * 1441
    current = 0

    for minute in range(1441):
        current += change[minute]
        open_store[minute] = current

    times = list(map(int, input().split()))
    result = []

    for index in range(check):
        result.append(str(open_store[times[index]]))

    print(" ".join(result))


main()
