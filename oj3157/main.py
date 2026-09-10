"""Point accumulation game"""

def main():
    """Point accumulation game"""
    n = int(input())
    total = 0
    for _ in range(n):
        action = input()
        if action == "+":
            total += 10
        elif action == "-":
            total -= 5
    print(total)

main()
