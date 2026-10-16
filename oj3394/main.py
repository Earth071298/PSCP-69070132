"""Forward Message"""
def main():
    """Forward Message"""
    n, start = map(int, input().split())

    students = []
    for _ in range(n):
        students.append(int(input()))

    visited = set()
    current = start

    while current and current not in visited:
        visited.add(current)
        current = students[current - 1]

    print(len(visited))

main()
