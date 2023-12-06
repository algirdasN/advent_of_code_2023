def split_to_int(string, separator):
    return [int(x) for x in string.split(separator) if x]


def main():
    with open("data/6.txt") as file:
        lines = file.read().split("\n")

    time = split_to_int(lines[0].split(":")[1], " ")
    dist = split_to_int(lines[1].split(":")[1], " ")

    total = 1
    for i in range(len(time)):
        win_count = 0
        for j in range(time[i]):
            if (time[i] - j) * j > dist[i]:
                win_count += 1
        total *= win_count

    print(total)

    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    first = 0
    second = time // 2

    while second - first > 1:
        middle = (first + second) // 2
        if (time - middle) * middle > dist:
            second = middle
        else:
            first = middle

    print(time + 1 - 2 * second)

if __name__ == "__main__":
    main()
