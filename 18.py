from collections import defaultdict


def main():
    with open("data/18.txt") as file:
        instructions = file.read().split("\n")

    dir_map = {
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
        "U": (-1, 0)
    }
    directions = [x.split(" ")[:2] for x in instructions]
    visited = defaultdict(set)

    curr = (0, 0)
    visited[curr[0]].add(curr[1])
    for d in directions:
        for i in range(int(d[1])):
            curr = (curr[0] + dir_map[d[0]][0], curr[1] + dir_map[d[0]][1])
            visited[curr[0]].add(curr[1])

    filled = defaultdict(set)
    for k in sorted(visited):
        s_v = sorted(visited[k])
        start = s_v[0]
        inner = True
        for i in range(1, len(s_v)):
            if s_v[i] == s_v[i - 1] + 1:
                continue

            if s_v[i - 1] != start:
                filled[k].update(range(start, s_v[i - 1] + 1))
                inner = all(x in filled[k - 1] for x in range(s_v[i - 1], s_v[i]))

            if inner:
                filled[k].update(range(s_v[i - 1], s_v[i] + 1))
            inner = not inner
            start = s_v[i]

        if start != s_v[-1]:
            filled[k].update(range(start, s_v[-1] + 1))

    print(sum(len(x) for x in filled.values()))


if __name__ == "__main__":
    main()
