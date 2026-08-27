"""RectangleArea"""

def main():
    """RectangleArea"""

    xA, yA, widthA, longA = map(int, input().split())
    xB, yB, widthB, longB = map(int, input().split())

    left = max(xA, xB)
    right = min(xA + widthA, xB + widthB)

    bottom = max(yA, yB)
    top = min(yA + longA, yB + longB)

    width = right - left
    height = top - bottom

    if width <= 0 or height <= 0:
        print("no overlapping")
    else:
        print(width * height)

main()
