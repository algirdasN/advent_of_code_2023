def split_to_int(string, separator):
    return [int(x) for x in string.split(separator) if x]


def main():
    with open("data/5.txt") as file:
        lines = file.read().split("\n\n")

    seeds = split_to_int(lines[0].split(":")[1], " ")

    mappings = []
    for line in lines[1:]:
        instr = [split_to_int(x, " ") for x in line.split(":\n")[1].split("\n")]
        mappings.append({range(x[1], x[1] + x[2]): x[0] - x[1] for x in instr})

    for mapping in mappings:
        for i, s in enumerate(seeds):
            for k, v in mapping.items():
                if s in k:
                    seeds[i] += v
                    break

    print(min(seeds))

    seeds = split_to_int(lines[0].split(":")[1], " ")
    seeds = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for mapping in mappings:
        to_check = list(seeds)
        while to_check:
            s = to_check.pop()
            for k, v in mapping.items():
                if s.stop <= k.start or s.start >= k.stop:
                    continue

                seeds.remove(s)
                if s.start >= k.start and s.stop <= k.stop:
                    seeds.append(range(s.start + v, s.stop + v))
                    break
                if s.start < k.start <= s.stop:
                    first = range(s.start, k.start)
                    second = range(k.start, s.stop)
                if s.start <= k.stop < s.stop:
                    first = range(s.start, k.stop)
                    second = range(k.stop, s.stop)
                seeds.append(first)
                seeds.append(second)
                to_check.append(first)
                to_check.append(second)
                break

    print(min(x.start for x in seeds))


if __name__ == "__main__":
    main()
