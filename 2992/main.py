"""inverse number input number and add that both"""

number = int(input())
symbol = input()

inverse_number = str(number)
inverse_number = inverse_number[::-1]
reverse_number = int(inverse_number)

if symbol == "+":
    print(number, "+", reverse_number, "=", number + reverse_number)
elif symbol == "*":
    print(number, "*", reverse_number, "=", number * reverse_number)
