def main():
    with open("data/21.txt") as file:
        grid = file.read().split("\n")

    dir_map = ((0, 1), (1, 0), (0, -1), (-1, 0))

    moves = set()
    for i in range(len(grid)):
        if "S" in grid[i]:
            moves.add((i, grid[i].index("S")))

    for i in range(65):
        next_moves = set()
        valid_moves = 0
        while moves:
            curr = moves.pop()
            if grid[curr[0]][curr[1]] == "#":
                continue

            valid_moves += 1
            for d in dir_map:
                next_moves.add((curr[0] + d[0], curr[1] + d[1]))
        moves = next_moves

    print(valid_moves)


if __name__ == "__main__":
    main()
