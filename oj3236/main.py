"""twin code"""

def main():
    """check tech twins"""
    n = int(input())
    code_1 = input()
    code_2 = input()

    wrong = 0

    for i in range(n):
        if int(code_1[i]) + int(code_2[i]) != 9:
            wrong += 1

    if not wrong:
        print("YES")
    else:
        print("NO", wrong)

main()
