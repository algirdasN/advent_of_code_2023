from collections import deque, defaultdict


def build_graph(grid, start, end, directed):
    graph = defaultdict(dict)

    dir_map = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0)
    }

    move_queue = deque()
    move_queue.append(((1, start[1]), start, (1, 0), 1, True))

    while move_queue:
        curr, prev, last_dir, move, both_way = move_queue.pop()

        if curr == end:
            graph[prev][end] = move
            continue

        if prev in graph and curr in graph[prev]:
            continue

        valid_dir = []
        for d in dir_map.values():
            if d[0] == -last_dir[0] and d[1] == -last_dir[1]:
                continue

            if grid[curr[0] + d[0]][curr[1] + d[1]] == "#":
                continue

            cell = grid[curr[0]][curr[1]]
            if directed and cell in dir_map:
                if d != dir_map[cell]:
                    continue
                else:
                    both_way = False

            valid_dir.append(d)

        match len(valid_dir):
            case 0:
                continue
            case 1:
                d = valid_dir[0]
                move_queue.append(((curr[0] + d[0], curr[1] + d[1]), prev, d, move + 1, both_way))
            case _:
                graph[prev][curr] = move
                if prev[0] > 0 and both_way:
                    graph[curr][prev] = move
                for d in valid_dir:
                    move_queue.append(((curr[0] + d[0], curr[1] + d[1]), curr, d, 1, True))

    return graph


def get_max_moves(graph, start, end):
    visited = []
    max_move = 0

    move_queue = deque()
    move_queue.append((start, 0, 0))

    while move_queue:
        curr, index, total = move_queue.pop()

        if curr == end:
            max_move = max(max_move, total)
            continue

        visited[index:] = []

        if curr in visited:
            continue

        visited.append(curr)

        for k, v in graph[curr].items():
            move_queue.append((k, index + 1, total + v))

    return max_move


def main():
    with open("data/23.txt") as file:
        grid = file.read().split("\n")

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    d_graph = build_graph(grid, start, end, True)
    print(get_max_moves(d_graph, start, end))

    graph = build_graph(grid, start, end, False)
    print(get_max_moves(graph, start, end))


if __name__ == "__main__":
    main()
