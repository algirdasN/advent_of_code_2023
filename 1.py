import re


def main():
    with open("data/1.txt") as file:
        lines = file.readlines()

    total = 0
    pattern_first = re.compile(r"^\D*(\d)")
    pattern_last = re.compile(r"(\d)\D*$")
    for i in lines:
        first = pattern_first.search(i).group(1)
        second = pattern_last.search(i).group(1)
        total += int(first + second)

    print(total)

    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    total = 0
    pattern_first = re.compile(r"^.*?(\d|" + "|".join(digits.keys()) + r")")
    pattern_last = re.compile(r".*(\d|" + "|".join(digits.keys()) + r").*?$")
    for i in lines:
        first = pattern_first.search(i).group(1)
        second = pattern_last.search(i).group(1)
        total += int(digits.get(first, first) + digits.get(second, second))

    print(total)


if __name__ == "__main__":
    main()
