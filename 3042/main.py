"""/10"""

number = int(input())

a = number - (number % 10)
result = []

while a >= 0 :
    result.append(str(a))
    a -= 10

print(" ".join(result))
