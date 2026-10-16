
"""Array 2D checker"""

def main():
    """Array 2D checker"""
    arr = []

    for _ in range(5):
        row = list(map(int, input().split()))
        arr.append(row)

    odd_row = -1
    odd_col = -1

    for i in range(5):
        if sum(arr[i]) % 2:
            odd_row = i

    for j in range(5):
        total = 0
        for i in range(5):
            total += arr[i][j]

        if total % 2:
            odd_col = j

    if odd_row != -1 and odd_col != -1:
        print(odd_row, odd_col)
    else:
        print(-1, -1)

main()
