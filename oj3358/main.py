"""pair pig"""

def main():
    """cal pair pig"""
    pairs = int(input())
    weights = list(map(int, input().split()))

    result = []

    for index in range(0, pairs * 2, 2):
        heavier = max(weights[index], weights[index + 1])
        result.append(heavier)

    if pairs == 1:
        print(result[0])
    else:
        print(" + ".join(map(str, result)), "=", sum(result))

main()
