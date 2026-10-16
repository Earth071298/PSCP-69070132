"""Queue Chair Height."""
def main():
    """Calculate the minimum chair height for each customer."""
    n, _ = map(int, input().split())
    heights = list(map(int, input().split()))
    customers = list(map(int, input().split()))

    max_height = 0

    for i in range(n):
        if i + 1 in customers:
            chair = max(0, max_height - heights[i] + 1)
            print(chair)

        if heights[i] > max_height:
            max_height = heights[i]

main()
