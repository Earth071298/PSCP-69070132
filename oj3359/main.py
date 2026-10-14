"""Find the minimum number of bowl stacks."""

def main():
    """Count the maximum frequency of any bowl size."""

    bowls = int(input())
    counts = [0] * 301

    for _ in range(bowls):
        size = int(input())
        counts[size] += 1

    print(max(counts))

main()
