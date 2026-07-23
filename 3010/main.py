"""Find the Quadrant"""

x_axis = int(input())
y_axis = int(input())

if x_axis == 0 and y_axis == 0:
    print("O")
elif x_axis == 0:
    print("Y")
elif y_axis == 0:
    print("X")
elif x_axis > 0 and y_axis > 0:
    print("Q1")
elif x_axis < 0 and y_axis > 0:
    print("Q2")
elif x_axis < 0 and y_axis < 0:
    print("Q3")
else:
    print("Q4")
