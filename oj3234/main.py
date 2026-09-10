"""Christmas lights"""

def main():
    """Christmas lights"""
    color, number = input().split()
    number = int(number)

    colors = ["R", "G", "B"]
    names = {
        "R": "Red",
        "G": "Green",
        "B": "Blue"
    }
    start = colors.index(color)

    for i in range(number):
        print(names[colors[(start + i) % 3]], end=" ")

main()
