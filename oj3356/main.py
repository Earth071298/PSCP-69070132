"""Bus seating plan"""

def main():
    """Display the bus seating plan"""

    seats = int(input())
    rows = int(input())
    target = int(input())

    for row in range(seats, 0, -1):
        line = []

        for col in range(rows):
            number = row + col * seats

            if number == target:
                line.append("XX")
            else:
                line.append(f"{number:02d}")

        print(" ".join(line))

        if row > 1 and row % 2 == 1:
            print()

main()
