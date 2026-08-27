"""Number of vowels"""

def main():
    """Number of vowels"""
    n = int(input())
    count = 0

    for _ in range(n):
        char = input()

        if char in "AEIOU":
            count += 1

    print(count)

main()
