def main():
    with open("data/11.txt") as file:
        lines = file.read().split("\n")

    grid = []
    galaxies = []
    for i, line in enumerate(lines):
        grid.append([])
        for j, point in enumerate(line):
            grid[i].append(point)
            if point == "#":
                galaxies.append((i, j))

    expand_rows = []
    for i in range(len(grid)):
        if all(x == "." for x in grid[i]):
            expand_rows.append(i)

    expand_cols = []
    for i in range(len(grid[0])):
        if all(x == "." for x in [y[i] for y in grid]):
            expand_cols.append(i)

    m_galaxies = []
    m_galaxies2 = []
    for g in galaxies:
        i = j = 0
        for i in range(len(expand_rows)):
            if expand_rows[i] > g[0]:
                break
        else:
            i += 1
        for j in range(len(expand_cols)):
            if expand_cols[j] > g[1]:
                break
        else:
            j += 1
        m_galaxies.append((g[0] + i, g[1] + j))
        m_galaxies2.append((g[0] + i * (1_000_000 - 1), g[1] + j * (1_000_000 - 1)))

    total = 0
    total2 = 0
    for i in range(len(m_galaxies)):
        for j in range(i + 1, len(m_galaxies)):
            total += abs(m_galaxies[i][0] - m_galaxies[j][0]) + abs(m_galaxies[i][1] - m_galaxies[j][1])
            total2 += abs(m_galaxies2[i][0] - m_galaxies2[j][0]) + abs(m_galaxies2[i][1] - m_galaxies2[j][1])

    print(total)
    print(total2)


if __name__ == "__main__":
    main()
