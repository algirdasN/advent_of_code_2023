import math
import re


def main():
    with open("data/8.txt") as file:
        lines = file.read().split("\n")

    moves = lines[0].replace("L", "0").replace("R", "1")

    mapping = {y[0]: eval(re.sub(r"([A-Z]{3})", r"'\1'", y[1])) for y in [x.split(" = ") for x in lines[2:]]}

    current = "AAA"
    count = 0

    while current != "ZZZ":
        current = mapping[current][int(moves[count % len(moves)])]
        count += 1

    print(count)

    start = [x for x in mapping if x.endswith("A")]
    exits = []

    for s in start:
        current = s
        count = 0

        while not current.endswith("Z"):
            current = mapping[current][int(moves[count % len(moves)])]
            count += 1

        exits.append(count)

    print(math.lcm(*exits))


if __name__ == "__main__":
    main()
