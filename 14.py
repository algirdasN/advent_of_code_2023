from collections import defaultdict
from itertools import count


def move_h(grid, forward=False):
    new_grid = [["."] * len(c) for c in grid]
    for i, c in enumerate(grid):
        rock_map = defaultdict(int)
        next_empty = 0 + forward * (len(c) - 1)
        for j in range(next_empty, len(c) - next_empty - 2 * forward, 1 - 2 * forward):
            if c[j] == "#":
                next_empty = j + (1 - 2 * forward)
                new_grid[i][j] = "#"
            if c[j] == "O":
                rock_map[next_empty] += 1

        for k, v in rock_map.items():
            new_grid[i][k - (v - 1) * forward: k + 1 + (v - 1) * (not forward)] = ["O"] * v

    return new_grid


def move_v(grid, forward=False):
    grid_t = list(zip(*grid))
    new_grid_t = move_h(grid_t, forward)
    return list(zip(*new_grid_t))


def get_weight(grid):
    return sum((len(grid) - i) * r.count("O") for i, r in enumerate(grid))


def get_state(grid):
    return bytes(1 if x == "O" else 0 for row in grid for x in row)


def main():
    with open("data/14.txt") as file:
        grid = [list(x) for x in file.read().split("\n")]

    print(get_weight(move_v(grid)))

    weights = []
    states = []
    for i in count():
        grid = move_v(grid, False)
        grid = move_h(grid, False)
        grid = move_v(grid, True)
        grid = move_h(grid, True)
        weights.append(get_weight(grid))

        new_state = get_state(grid)
        try:
            j = len(states) - states.index(new_state)
        except ValueError:
            states.append(new_state)
            continue

        print(weights[-j:][(1_000_000_000 - i) % j - 2])
        break


if __name__ == "__main__":
    main()
