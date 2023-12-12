import re


def build_pattern(counts):
    return r"^[^#]*" + r"[^#]+".join(f"[#?]{{{x}}}" for x in counts) + r"[^#]*$"


def count_matches(pattern, string):
    match = pattern.match(string)
    if not match:
        return 0

    if "?" not in string:
        return 1

    first = string.replace("?", ".", 1)
    second = string.replace("?", "#", 1)

    return count_matches(pattern, first) + count_matches(pattern, second)


def main():
    with open("data/12.txt") as file:
        lines = file.read().split("\n")

    rows = []
    patterns = []

    for line in lines:
        ll = line.split(" ")
        rows.append(ll[0])

        p1 = build_pattern(ll[1].split(","))
        patterns.append(re.compile(p1))

    total = 0
    for i in range(len(rows)):
        total += count_matches(patterns[i], rows[i])

    print(total)


if __name__ == "__main__":
    main()
