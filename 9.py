def delta(seq):
    return [seq[i] - seq[i + 1] for i in range(len(seq) - 1)]


def dual_seq(seq):
    result = []
    while seq:
        result.append(seq[0])
        seq = delta(seq)
    return result


def extra_pol(seq, n):
    return dual_seq(dual_seq(seq) + [0] * n)


def main():
    with open("data/9.txt") as file:
        lines = file.read().split("\n")

    total = 0
    for line in lines:
        seq = [int(x) for x in line.split(" ")]
        total += extra_pol(seq, 1)[-1]

    print(total)

    total = 0
    for line in lines:
        seq = [int(x) for x in line.split(" ")]
        seq.reverse()
        total += extra_pol(seq, 1)[-1]

    print(total)


if __name__ == "__main__":
    main()
