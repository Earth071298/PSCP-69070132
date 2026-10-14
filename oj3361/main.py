
"""Count car models that can never be sold."""

def main():
    """Find cars dominated by cheaper, more efficient models."""

    count = int(input())
    cars = []

    for _ in range(count):
        price, efficiency = map(int, input().split())
        cars.append((price, efficiency))

    max_efficiency = 0
    unsold = 0

    for _, efficiency in reversed(cars):
        if efficiency < max_efficiency:
            unsold += 1
        else:
            max_efficiency = efficiency

    print(unsold)

main()
