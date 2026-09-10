"""draw x-shape"""

def main():
    """draw x-shape"""
    x, k = input().split()
    x = int(x)

    middle = x // 2

    for row in range(x):
        line = ""

        for col in range(x):
            if col in (row, x - 1 - row):
                if k == "#":
                    line += "#"
                else:
                    distance = abs(middle - row)
                    line += chr(ord(k) + distance)
            else:
                line += "-"

        print(line)

main()
