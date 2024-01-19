from collections import deque, defaultdict


def build_graph(grid):
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))
    graph = defaultdict(dict)

    dir_map = ((0, 1), (1, 0), (0, -1), (-1, 0))

    move_queue = deque()
    move_queue.append(((1, start[1]), start, (1, 0), 1))

    while move_queue:
        curr, prev, last_dir, move = move_queue.pop()

        if curr == end:
            graph[prev][end] = move
            continue

        if prev in graph and curr in graph[prev]:
            continue

        valid_dir = []
        for d in dir_map:
            if d[0] == -last_dir[0] and d[1] == -last_dir[1]:
                continue

            if grid[curr[0] + d[0]][curr[1] + d[1]] == "#":
                continue

            valid_dir.append(d)

        match len(valid_dir):
            case 0:
                continue
            case 1:
                d = valid_dir[0]
                move_queue.append(((curr[0] + d[0], curr[1] + d[1]), prev, d, move + 1))
            case _:
                graph[prev][curr] = move
                if prev[0] > 0:
                    graph[curr][prev] = move
                for d in valid_dir:
                    move_queue.append(((curr[0] + d[0], curr[1] + d[1]), curr, d, 1))

    return graph


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

    graph = build_graph(grid)
    visited = []

    move_queue = deque()
    move_queue.append((start, 0, 0))

    max_move = 0

    while move_queue:
        curr, index, total = move_queue.pop()

        if curr == end:
            if total > max_move:
                max_move = total
            continue

        if index < len(visited):
            visited[index:] = []

        if curr in visited:
            continue

        visited.append(curr)

        for k, v in graph[curr].items():
            move_queue.append((k, index + 1, total + v))

    print(max_move)


if __name__ == "__main__":
    main()
