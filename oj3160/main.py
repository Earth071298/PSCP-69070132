"""find prime number"""

def main():
    """find prime number"""
    first, last = map(int, input().split())
    primes = []

    for num in range(first, last + 1):
        if num < 2:
            continue
        prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                prime = False
                break
        if prime:
            primes.append(num)

    if primes:
        print(*primes)
    print("Total primes:", len(primes))

main()
