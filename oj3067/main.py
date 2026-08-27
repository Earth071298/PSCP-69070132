"""Increasing/decreasing"""

def main():
    """Increasing/decreasing"""
    a = float(input())
    b = float(input())
    c = float(input())

    if a < b < c:
        print("increasing")
    elif a > b > c:
        print("decreasing")
    else:
        print("neither")

main()
