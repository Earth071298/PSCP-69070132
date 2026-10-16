"""Day08-0_02-Backward"""
def main():
    """Day08-0_02-Backward"""
    result = []
    while True:
        text = input()
        if text == "NULL":
            break
        result.append(text)
    result.reverse()
    print("\n".join(result))

main()
