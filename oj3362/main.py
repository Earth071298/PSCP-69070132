
"""Create a lucky charm for a couple."""

def main():
    """Generate the charm from two names."""

    name_one = input().lower()
    name_two = input().lower()

    length = max(len(name_one), len(name_two))

    name_one = (name_one * (length // len(name_one) + 1))[:length]
    name_two = (name_two * (length // len(name_two) + 1))[:length]

    charm = ""

    for char_one, char_two in zip(name_one, name_two):
        if char_one in "love" or char_two in "love":
            charm += "w"
        else:
            charm += "$"

    w_count = charm.count("w")
    longest = max(
        (len(group) for group in charm.split("$")),
        default=0
    )

    if w_count % 2 == 1:
        charm += str(longest)
    elif "ww" not in charm:
        charm += "#"

    print(charm)

main()
