"""Smart Trash Collector"""

def main():
    """Smart Trash Collector"""
    n = int(input())

    for _ in range(n):
        plastic, can, glass = map(float, input().split())
        total = plastic + can + glass
        result = [f"{total:.1f}"]

        if total > 50:
            result.append("Overloaded")

        if plastic > 20:
            result.append("Check Type Plastic")

        if can > 20:
            result.append("Check Type Can")

        if glass > 20:
            result.append("Check Type Glass")

        print(", ".join(result))

main()
