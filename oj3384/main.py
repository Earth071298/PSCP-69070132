"""PickThem"""

import ast

def main():
    """PickThem"""
    nums = ast.literal_eval(input())
    found = False

    for num in nums:
        if not num % 2:
            print(num)
            found = True

    if not found:
        print("Nope")

main()
