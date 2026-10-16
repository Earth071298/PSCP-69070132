"""Difference"""

def main():
    """Difference"""
    n = int(input())
    m = int(input())

    set_a = set()
    set_b = set()

    for _ in range(n):
        set_a.add(int(input()))

    for _ in range(m):
        set_b.add(int(input()))

    result = sorted(set_a - set_b)
    print(*result)


main()
