def reflect_x(rocks, column, min_col, max_col):
    pre = set()
    post = set()
    for r in rocks:
        if 2 * column - max_col - 2 < r[0] < column:
            pre.add(r)
            continue

        if column <= r[0] < 2 * column - min_col:
            post.add((2 * column - r[0] - 1, r[1]))
            continue

    return pre, post


def reflect_y(rocks, row, min_row, max_row):
    pre = set()
    post = set()
    for r in rocks:
        if 2 * row - max_row - 2 < r[1] < row:
            pre.add(r)
            continue

        if row <= r[1] < 2 * row - min_row:
            post.add((r[0], 2 * row - r[1] - 1))
            continue

    return pre, post


def main():
    with open("data/13.txt") as file:
        grids = [x.split("\n") for x in file.read().split("\n\n")]

    rock_maps = []
    for g in grids:
        rock_maps.append(set())
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == "#":
                    rock_maps[-1].add((i, j))

    total = 0
    total2 = 0
    for g, m in zip(grids, rock_maps):
        for i in range(1, len(g)):
            pre, post = reflect_x(m, i, 0, len(g) - 1)
            total += 100 * i * (pre == post)
            total2 += 100 * i * (len(pre ^ post) == 1)

        for i in range(1, len(g[0])):
            pre, post = reflect_y(m, i, 0, len(g[0]) - 1)
            total += i * (pre == post)
            total2 += i * (len(pre ^ post) == 1)

    print(total)
    print(total2)


if __name__ == "__main__":
    main()
