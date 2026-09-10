"""lottery"""

def main():
    """lottery"""
    win_letter, win_number = input().split()
    ticket_letter, ticket_number = input().split()

    if win_letter == ticket_letter and win_number == ticket_number:
        prize = 1000000
    elif win_number == ticket_number:
        prize = 100000
    elif win_letter == ticket_letter and win_number[-3:] == ticket_number[-3:]:
        prize = 2000
    elif win_letter == ticket_letter and win_number[-2:] == ticket_number[-2:]:
        prize = 1000
    elif win_number[-3:] == ticket_number[-3:]:
        prize = 200
    elif win_number[-2:] == ticket_number[-2:]:
        prize = 100
    elif win_letter == ticket_letter:
        prize = 20
    else:
        prize = 0

    print(prize)

main()
