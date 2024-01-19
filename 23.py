from collections import deque


def main():
    with open("data/23.txt") as file:
        grid = file.read().split("\n")

    dir_map = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0)
    }
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    visited = []

    move_queue = deque()
    move_queue.append((start, 0))

    max_move = 0

    while move_queue:
        curr, move = move_queue.pop()
        if curr[0] not in range(len(grid)) or curr[1] not in range(len(grid[0])):
            continue

        if curr == end:
            max_move = max(max_move, move)
            continue

        if grid[curr[0]][curr[1]] == "#":
            continue

        if curr in visited:
            continue

        if move < len(visited):
            visited[move:] = []

        visited.append(curr)

        if grid[curr[0]][curr[1]] in dir_map:
            d = dir_map[grid[curr[0]][curr[1]]]
            move_queue.append(((curr[0] + d[0], curr[1] + d[1]), move + 1))
        else:
            for d in dir_map.values():
                move_queue.append(((curr[0] + d[0], curr[1] + d[1]), move + 1))

    print(max_move)


if __name__ == "__main__":
    main()
