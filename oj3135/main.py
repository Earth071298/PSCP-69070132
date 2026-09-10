"""Institutions and Thieves"""

def main():
    """Institutions and Thieves"""
    n, k, t = map(int, input().split())

    person = 1
    count = 1

    if t == 1:
        print(1)
    else:
        while True:
            person = (person + k - 1) % n + 1
            if person == 1:
                break
            count += 1
            if person == t:
                break
        print(count)

main()
