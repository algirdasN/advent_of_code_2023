import re
from collections import OrderedDict


def hash_string(string):
    total = 0
    for c in string:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def main():
    with open("data/15.txt") as file:
        instructions = file.readline().split(",")

    total = 0
    for i in instructions:
        total += hash_string(i)

    print(total)

    pattern = re.compile(r"(\w+)(-|=(\d+))")
    boxes = [OrderedDict() for _ in range(256)]

    for inst in instructions:
        match = pattern.match(inst)
        lens = match.group(1)
        index = hash_string(lens)
        if "=" in inst:
            f_length = int(match.group(3))
            boxes[index][lens] = f_length
        elif lens in boxes[index]:
            boxes[index].pop(lens)

    total = 0
    for i, b in enumerate(boxes):
        total += sum((i + 1) * (j + 1) * x for j, x in enumerate(b.values()))

    print(total)


if __name__ == "__main__":
    main()
