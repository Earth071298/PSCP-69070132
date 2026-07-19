"""Mix colors"""

colors1 = input().strip()
colors2 = input().strip()

primary_colors = ["Red", "Yellow", "Blue"]

if colors1 not in primary_colors or colors2 not in primary_colors:
    print("Error")
elif colors1 == colors2:
    print(colors1)
else:
    mix = {colors1, colors2}
    if mix == {"Red", "Yellow"}:
        print("Orange")
    elif mix == {"Red", "Blue"}:
        print("Violet")
    elif mix == {"Yellow", "Blue"}:
        print("Green")
