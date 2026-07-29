"""Temperature is measured in Fahrenheit (F), Celsius (K), and Rankine (R) units, derived from Celsius (C)."""

temp = float(input())
Start_unit = input()
last_unit = input()

if Start_unit == "C":
    c = temp
elif Start_unit == "K":
    c = temp - 273.15
elif Start_unit == "F":
    c = (temp - 32) * 5/9
elif Start_unit == "R":
    c = (temp  - 491.67) * 5/9

if last_unit == "C":
    result = c
elif last_unit == "K":
    result = c + 273.15
elif last_unit == "F":
    result = (c * 9/5) + 32
elif last_unit == "R":
    result = (c + 273.15) * 9/5

print(f"{result:.2f}")
