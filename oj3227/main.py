"""44 cards"""

def main():
    """convert card"""
    card = input().upper()

    point = card[:-1]
    suit = card[-1]

    point_name = {
        "A": "ace",
        "J": "jack",
        "Q": "queen",
        "K": "king"
    }

    suit_name = {
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
        "C": "clubs"
    }

    point = point_name.get(point, point)
    suit = suit_name.get(suit, suit)

    print(point, "of", suit)

main()
