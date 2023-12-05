import re
from collections import defaultdict


def main():
    with open("data/3.txt") as file:
        lines = file.readlines()

    num_pattern = re.compile(r"\d+")
    symbol_pattern = re.compile(r"[^0-9.]")

    total = 0
    for i in range(len(lines)):
        matches = num_pattern.finditer(lines[i])
        for m in matches:
            start = m.start()
            end = m.end()
            lookup_start = max(0, start - 1)
            lookup_end = min(len(lines[i]), end + 1)

            if (start > 0 and symbol_pattern.search(lines[i][start - 1])) or \
                    (end < len(lines[i]) - 1 and symbol_pattern.search(lines[i][end])) or \
                    (i > 0 and symbol_pattern.search(lines[i - 1][lookup_start:lookup_end])) or \
                    (i < len(lines) - 1 and symbol_pattern.search(lines[i + 1][lookup_start:lookup_end])):
                total += int(m.group(0))

    print(total)

    gears = defaultdict(list)
    for i in range(len(lines)):
        matches = num_pattern.finditer(lines[i])
        for m in matches:
            start = m.start()
            end = m.end()
            value = int(m.group(0))

            if start > 0 and "*" == lines[i][start - 1]:
                gears[(i, start - 1)].append(value)
                continue

            if end < len(lines[i]) - 1 and "*" == lines[i][end]:
                gears[(i, end)].append(value)
                continue

            lookup_start = max(0, start - 1)
            lookup_end = min(len(lines[i]), end + 1)

            if i > 0 and "*" in lines[i - 1][lookup_start:lookup_end]:
                gears[(i - 1, start - 1 + lines[i - 1][lookup_start:lookup_end].index("*"))].append(value)
                continue

            if i < len(lines) - 1 and "*" in lines[i + 1][lookup_start:lookup_end]:
                gears[(i + 1, start - 1 + lines[i + 1][lookup_start:lookup_end].index("*"))].append(value)
                continue

    print(sum(i[0] * i[1] for i in gears.values() if len(i) == 2))


if __name__ == "__main__":
    main()
