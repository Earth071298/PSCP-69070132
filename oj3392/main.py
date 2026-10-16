"""Array Ha He."""

def main():
    """Array Ha He"""
    numbers = []

    for i in range(3):
        num = int(input())
        numbers.append(num)
        print(f"Input number {i + 1} stored.")

    while True:
        choice = int(input())

        if not choice:
            break

        if choice == 1:
            print("Original order:", *numbers)
        elif choice == 2:
            print("Descending order:", *sorted(numbers, reverse=True))
        elif choice == 3:
            print("Ascending order:", *sorted(numbers))

main()
