"""Duplicate I"""

def main():
    """Duplicate I"""
    m = int(input())
    n = int(input())

    group_a = set()
    group_b = set()

    for _ in range(m):
        group_a.add(input())

    for _ in range(n):
        group_b.add(input())

    duplicates = sorted(group_a & group_b, reverse=True)

    if duplicates:
        for student_id in duplicates:
            print(student_id)
    else:
        print("Nope")

main()
