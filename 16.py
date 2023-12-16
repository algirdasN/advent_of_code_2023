from collections import defaultdict


def get_visited(grid, start, start_dir):
    visited = defaultdict(list)
    queue = [(start, start_dir)]

    while queue:
        c, d = queue.pop()
        if d in visited[c]:
            continue

        visited[c].append(d)
        curr = grid[c[0]][c[1]]
        new_d = None

        if curr == "|" and d[0] == 0:
            d = (1, 0)
            new_d = (-1, 0)
        if curr == "-" and d[1] == 0:
            d = (0, 1)
            new_d = (0, -1)
        if curr == "\\":
            d = (d[1], d[0])
        if curr == "/":
            d = (-d[1], -d[0])

        if 0 <= c[0] + d[0] < len(grid) and 0 <= c[1] + d[1] < len(grid[0]):
            queue.append(((c[0] + d[0], c[1] + d[1]), d))
        if new_d and 0 <= c[0] + new_d[0] < len(grid) and 0 <= c[1] + new_d[1] < len(grid[0]):
            queue.append(((c[0] + new_d[0], c[1] + new_d[1]), new_d))

    return visited


def main():
    with open("data/16.txt") as file:
        grid = file.read().split("\n")

    visited = get_visited(grid, (0, 0), (0, 1))

    print(len(visited))

    games = []
    games.extend(((x, 0), (0, 1)) for x in range(len(grid)))
    games.extend(((x, len(grid[0]) - 1), (0, -1)) for x in range(len(grid)))
    games.extend(((0, x), (1, 0)) for x in range(len(grid[0])))
    games.extend(((len(grid) - 1, x), (-1, 0)) for x in range(len(grid[0])))

    maximum = 0
    for g in games:
        visited = get_visited(grid, g[0], g[1])
        maximum = max(maximum, len(visited))

    print(maximum)


if __name__ == "__main__":
    main()
