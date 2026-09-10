"""Fat rabbit"""

def main():
    """Fat rabbit"""
    count = int(input())
    overweight = 0
    max_weight = 0
    max_name = ""

    for _ in range(count):
        name, weight = input().split()
        weight = int(weight)

        if weight > 15:
            overweight += 1

        if weight > max_weight:
            max_weight = weight
            max_name = name

    print(overweight)
    print(max_name)

main()
