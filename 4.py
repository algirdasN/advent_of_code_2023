from collections import defaultdict


def split_to_set(string, separator):
    return {x for x in string.split(separator) if x}


def main():
    with open("data/4.txt") as file:
        lines = file.read().split("\n")

    total = 0
    for line in lines:
        card, winning = (split_to_set(x, " ") for x in line.split(": ")[1].split(" | "))
        matches = len(card.intersection(winning))
        if matches:
            total += 2 ** (matches - 1)

    print(total)

    cards = defaultdict(lambda: 1)

    for i in range(len(lines)):
        count = cards[i]
        card, winning = (split_to_set(x, " ") for x in lines[i].split(": ")[1].split(" | "))
        matches = len(card.intersection(winning))
        for j in range(matches):
            cards[i + j + 1] += count

    print(sum(cards.values()))


if __name__ == "__main__":
    main()
