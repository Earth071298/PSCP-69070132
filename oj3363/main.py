"""Calculate safe areas and infection risk in a city."""

def main():
    """Mark infection risks and count safe cells."""

    rows, cols = map(int, input().split())
    rabbit_row, rabbit_col = map(int, input().split())
    infected_count = int(input())

    grid = [[0] * cols for _ in range(rows)]

    for _ in range(infected_count):
        infected_row, infected_col = map(int, input().split())

        for row in range(max(0, infected_row - 2),
                         min(rows, infected_row + 3)):
            for col in range(max(0, infected_col - 2),
                             min(cols, infected_col + 3)):
                distance = max(
                    abs(row - infected_row),
                    abs(col - infected_col)
                )

                if not distance:
                    risk = 100
                elif distance == 1:
                    risk = 60
                else:
                    risk = 20

                grid[row][col] = max(grid[row][col], risk)

    safe_count = 0

    for row in range(rows):
        for col in range(cols):
            if not grid[row][col]:
                safe_count += 1

    print(safe_count)
    print(f"{grid[rabbit_row][rabbit_col]}%")

main()
