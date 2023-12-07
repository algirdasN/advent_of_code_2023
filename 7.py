from collections import Counter
from functools import cmp_to_key

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

for c in range(2, 10):
    card_ranks[str(c)] = c


def comparer(item1, item2):
    counter1 = Counter(item1)
    counter2 = Counter(item2)

    if len(counter1) != len(counter2):
        return (len(counter1) < len(counter2)) * 2 - 1

    values1 = counter1.most_common()
    values2 = counter2.most_common()

    for i in range(len(values1)):
        if values1[i][1] != values2[i][1]:
            return (values1[i][1] > values2[i][1]) * 2 - 1

    for i in range(len(item1)):
        if item1[i] != item2[i]:
            return (card_ranks[item1[i]] > card_ranks[item2[i]]) * 2 - 1

    return 0


card_ranks2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
}

for c in range(2, 10):
    card_ranks2[str(c)] = c


def comparer2(item1, item2):
    new1 = item1.replace("J", "")
    if new1:
        new1 += Counter(new1).most_common(1)[0][0] * (len(item1) - len(new1))
    else:
        new1 = item1

    new2 = item2.replace("J", "")
    if new2:
        new2 += Counter(new2).most_common(1)[0][0] * (len(item2) - len(new2))
    else:
        new2 = item2

    counter1 = Counter(new1)
    counter2 = Counter(new2)

    values1 = counter1.most_common()
    values2 = counter2.most_common()

    for i in range(len(values1)):
        if len(counter1) != len(counter2):
            return (len(counter1) < len(counter2)) * 2 - 1

    for i in range(len(values1)):
        if values1[i][1] != values2[i][1]:
            return (values1[i][1] > values2[i][1]) * 2 - 1

    for i in range(len(item1)):
        if item1[i] != item2[i]:
            return (card_ranks2[item1[i]] > card_ranks2[item2[i]]) * 2 - 1

    return 0


def main():
    with open("data/7.txt") as file:
        lines = file.read().split("\n")

    bets = {y[0]: int(y[1]) for y in [x.split(" ") for x in lines]}
    hands = list(bets.keys())

    hands.sort(key=cmp_to_key(comparer))

    print(sum(bets[x] * (i + 1) for i, x in enumerate(hands)))

    hands.sort(key=cmp_to_key(comparer2))

    print(sum(bets[x] * (i + 1) for i, x in enumerate(hands)))


if __name__ == "__main__":
    main()
