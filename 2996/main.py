"""สลับตัวอักษร"""

name = input()
name = name.lower()
x = -1
for i in range(5):
    print(name[x], end="")
    x -= 1
