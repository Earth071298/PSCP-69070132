
"""Find the two largest bread piece areas."""

def main():
    """Calculate the two largest areas after cutting bread."""

    width, height, _, _ = map(int, input().split())
    x_cuts = list(map(int, input().split()))
    y_cuts = list(map(int, input().split()))

    x_cuts = [0] + x_cuts + [width]
    y_cuts = [0] + y_cuts + [height]

    widths = []
    heights = []

    for index in range(len(x_cuts) - 1):
        widths.append(x_cuts[index + 1] - x_cuts[index])

    for index in range(len(y_cuts) - 1):
        heights.append(y_cuts[index + 1] - y_cuts[index])

    areas = []

    for piece_width in widths:
        for piece_height in heights:
            areas.append(piece_width * piece_height)

    areas.sort(reverse=True)
    print(areas[0], areas[1])


main()
