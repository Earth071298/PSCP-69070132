"""castle"""

from collections import deque
from math import isqrt

def get_neighbors(room):
    row = isqrt(room - 1)
    pos = room - row * row - 1
    neighbors = []
    if pos % 2 == 0:
        if pos > 0:
            neighbors.append(room - 1)

        if pos < 2 * row:
            neighbors.append(room + 1)
        neighbors.append((row + 1) ** 2 + pos + 1)

    else:
        neighbors.append(room - 1)

        if pos < 2 * row:
            neighbors.append(room + 1)

        if row > 0:
            neighbors.append((row - 1) ** 2 + pos)

    return neighbors


def main():
    n = int(input())

    if n == 1:
        print(0)
        return

    queue = deque([1])
    distance = {1: 0}

    while queue:
        room = queue.popleft()

        for next_room in get_neighbors(room):

            if next_room > n:
                continue

            if next_room not in distance:
                distance[next_room] = distance[room] + 1

                if next_room == n:
                    print(distance[next_room])
                    return

                queue.append(next_room)

main()
