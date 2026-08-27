"""AR TikTok"""

r, x, y = map(int, input().split())

distance = x**2 + y**2
radius = r**2

if distance < radius:
    print("IN")
elif distance == radius:
    print("ON")
else:
    print("OUT")
