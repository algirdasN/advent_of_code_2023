from collections import defaultdict


def consolidate_ranges(ranges):
    range_copy = [x for x in ranges]
    ranges.clear()

    count = 0
    while range_copy:
        r = range_copy.pop(0)
        for i in range(len(range_copy)):
            if range_copy[i].stop == r.start + 1 or range_copy[i].start + 1 == r.stop:
                count += 1
                other = range_copy.pop(i)
                range_copy.append(range(
                    min(other.start, r.start),
                    max(other.stop, r.stop)
                ))
                break
        else:
            ranges.append(r)

    return count


def get_area(directions):
    dir_map = {
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
        "U": (-1, 0)
    }

    curr = (0, 0)
    nodes = defaultdict(set)
    nodes[curr[0]].add(curr[1])

    for d in directions:
        curr = (curr[0] + int(d[1]) * dir_map[d[0]][0], curr[1] + int(d[1]) * dir_map[d[0]][1])
        nodes[curr[0]].add(curr[1])

    s_keys = sorted(nodes)
    s_values = sorted(nodes[s_keys[0]])
    active_ranges = [range(s_values[i], s_values[i + 1] + 1) for i in range(0, len(s_values), 2)]
    total = sum(len(x) for x in active_ranges)

    for i in range(1, len(s_keys)):
        total += (s_keys[i] - s_keys[i - 1]) * sum(len(x) for x in active_ranges)
        s_values = sorted(nodes[s_keys[i]])

        for j in range(0, len(s_values), 2):
            for k in range(len(active_ranges)):
                if s_values[j] == active_ranges[k].start and s_values[j + 1] == active_ranges[k].stop - 1:
                    active_ranges.pop(k)
                    break

                if s_values[j] == active_ranges[k].start:
                    active_ranges[k] = range(s_values[j + 1], active_ranges[k].stop)
                    break

                if s_values[j + 1] == active_ranges[k].stop - 1:
                    active_ranges[k] = range(active_ranges[k].start, s_values[j] + 1)
                    break

                if s_values[j + 1] == active_ranges[k].start or s_values[j] == active_ranges[k].stop - 1:
                    active_ranges[k] = range(
                        min(s_values[j], active_ranges[k].start),
                        max(s_values[j + 1] + 1, active_ranges[k].stop)
                    )
                    total += s_values[j + 1] - s_values[j]
                    break

                if s_values[j] > active_ranges[k].start and s_values[j + 1] < active_ranges[k].stop:
                    old = active_ranges.pop(k)
                    active_ranges.append(range(old.start, s_values[j] + 1))
                    active_ranges.append(range(s_values[j + 1], old.stop))
                    break

            else:
                active_ranges.append(range(s_values[j], s_values[j + 1] + 1))
                total += s_values[j + 1] - s_values[j] + 1

        total -= consolidate_ranges(active_ranges)

    return total


def main():
    with open("data/18.txt") as file:
        instructions = file.read().split("\n")

    directions = [x.split(" ")[:2] for x in instructions]

    print(get_area(directions))

    directions = []
    for i in instructions:
        x = i.split(" ")[2]
        directions.append(("RDLU"[int(x[-2])], int(x[2:-2], 16)))

    print(get_area(directions))


if __name__ == "__main__":
    main()
