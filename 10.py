from copy import copy

directions = {
    "|": {
        (1, 0): (1, 0),
        (-1, 0): (-1, 0),
        "left": {
            (1, 0): [(0, 1)],
            (-1, 0): [(0, -1)]
        },
        "right": {
            (1, 0): [(0, -1)],
            (-1, 0): [(0, 1)]
        }
    },
    "-": {
        (0, 1): (0, 1),
        (0, -1): (0, -1),
        "left": {
            (0, 1): [(-1, 0)],
            (0, -1): [(1, 0)]
        },
        "right": {
            (0, 1): [(1, 0)],
            (0, -1): [(-1, 0)]
        }
    },
    "L": {
        (1, 0): (0, 1),
        (0, -1): (-1, 0),
        "left": {
            (1, 0): [],
            (0, -1): [(0, -1), (1, 0)]
        },
        "right": {
            (1, 0): [(0, -1), (1, 0)],
            (0, -1): []
        }
    },
    "J": {
        (1, 0): (0, -1),
        (0, 1): (-1, 0),
        "left": {
            (1, 0): [(1, 0), (0, 1)],
            (0, 1): []
        },
        "right": {
            (1, 0): [],
            (0, 1): [(1, 0), (0, 1)]
        }
    },
    "7": {
        (-1, 0): (0, -1),
        (0, 1): (1, 0),
        "left": {
            (-1, 0): [],
            (0, 1): [(-1, 0), (0, 1)]
        },
        "right": {
            (-1, 0): [(-1, 0), (0, 1)],
            (0, 1): []
        }
    },
    "F": {
        (-1, 0): (0, 1),
        (0, -1): (1, 0),
        "left": {
            (-1, 0): [],
            (0, -1): []
        },
        "right": {
            (-1, 0): [],
            (0, -1): [(-1, 0), (0, -1)]
        }
    },
    ".": {}
}


def main():
    with open("data/10.txt") as file:
        grid = file.read().split("\n")

    for i, g in enumerate(grid):
        if "S" in g:
            j = g.index("S")
            start = i, j
            break

    n = []
    d = []
    for i in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= start[0] + i[0] < len(grid) and 0 <= start[1] + i[1] < len(grid[0]):
            pipe = grid[start[0] + i[0]][start[1] + i[1]]
            if i in directions[pipe]:
                n.append((start[0] + i[0], start[1] + i[1]))
                d.append(i)

    first, second = n
    f_dir, s_dir = d
    loop = {start, first, second}
    count = 1
    while first != second:
        f_dir = directions[grid[first[0]][first[1]]][f_dir]
        first = (first[0] + f_dir[0], first[1] + f_dir[1])
        s_dir = directions[grid[second[0]][second[1]]][s_dir]
        second = (second[0] + s_dir[0], second[1] + s_dir[1])
        loop.update({first, second})
        count += 1

    print(count)

    grid.append("0" * len(grid[0]))
    curr = n[0]
    curr_dir = d[0]
    left = set()
    right = set()
    while curr != start:
        curr_map = directions[grid[curr[0]][curr[1]]]

        for i in curr_map["left"][curr_dir]:
            if (0 <= curr[0] + i[0] < len(grid) and 0 <= curr[1] + i[1] < len(grid[0])
                    and (curr[0] + i[0], curr[1] + i[1]) not in loop):
                left.add((curr[0] + i[0], curr[1] + i[1]))

        for i in curr_map["right"][curr_dir]:
            if (0 <= curr[0] + i[0] < len(grid) and 0 <= curr[1] + i[1] < len(grid[0])
                    and (curr[0] + i[0], curr[1] + i[1]) not in loop):
                right.add((curr[0] + i[0], curr[1] + i[1]))

        curr_dir = curr_map[curr_dir]
        curr = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])

    def walk(this, parent_set):
        out = set()
        if this in loop or this in left or this in right:
            return out

        parent_set.add(this)
        for ii in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= this[0] + ii[0] < len(grid) and 0 <= this[1] + ii[1] < len(grid[0]):
                out.add((this[0] + ii[0], this[1] + ii[1]))
        return out

    queue = copy(left)
    left.clear()
    while queue:
        queue.update(walk(queue.pop(), left))

    queue = copy(right)
    right.clear()
    while queue:
        queue.update(walk(queue.pop(), right))

    print(len(left) if (len(grid), 0) in right else len(right))


if __name__ == "__main__":
    main()
