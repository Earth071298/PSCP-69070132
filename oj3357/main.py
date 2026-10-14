"""Magic giraffes"""

def main():
    """Count giraffes taller than their neighbors"""

    count = int(input())
    giraffes = [int(input()) for _ in range(count)]
    result = 0
    if count == 1:
        result = 1
    else:
        for i in range(count):
            if not i:
                if giraffes[i] > giraffes[i + 1]:
                    result += 1
            elif i == count - 1:
                if giraffes[i] > giraffes[i - 1]:
                    result += 1
            else:
                if (giraffes[i] > giraffes[i - 1]
                        and giraffes[i] > giraffes[i + 1]):
                    result += 1

    print(result)

main()
