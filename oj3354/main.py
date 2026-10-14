"""Hint filter for 3-digit numbers."""
def check_condition(digit, operator, hint):
    """Checker"""
    if operator == "==":
        result = digit == hint
    elif operator == ">":
        result = digit > hint
    elif operator == "<":
        result = digit < hint
    elif operator == ">=":
        result = digit >= hint
    elif operator == "<=":
        result = digit <= hint
    else:
        result = digit != hint

    return result

unit_op, unit_hint = input().split()
ten_op, ten_hint = input().split()
hundred_op, hundred_hint = input().split()

unit_hint = int(unit_hint)
ten_hint = int(ten_hint)
hundred_hint = int(hundred_hint)

for number in range(1000):
    hundred = number // 100
    ten = (number // 10) % 10
    unit = number % 10

    if (
        check_condition(unit, unit_op, unit_hint)
        and check_condition(ten, ten_op, ten_hint)
        and check_condition(hundred, hundred_op, hundred_hint)
    ):
        print(f"{number:03d}")
