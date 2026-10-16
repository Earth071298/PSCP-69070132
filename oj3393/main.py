"""Cave Explorer"""
def main():
    """Cave Explorer"""
    n = int(input())
    cave = input().split()

    pos = cave.index("1")
    treasure = cave.index("2")
    commands = input().strip()

    for command in commands:
        if command == "R":
            new_pos = pos + 1
        else:
            new_pos = pos - 1

        if new_pos < 0 or new_pos >= n:
            continue

        pos = new_pos

        if pos == treasure:
            break

    result = ["0"] * n
    result[treasure] = "2"
    result[pos] = "1"

    print(" ".join(result))

main()
