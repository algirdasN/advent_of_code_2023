import re


def main():
    with open("data/2.txt") as file:
        lines = file.readlines()

    max_dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    red_pattern = re.compile(r"(\d+) red")
    green_pattern = re.compile(r"(\d+) green")
    blue_pattern = re.compile(r"(\d+) blue")

    total = 0
    for line in lines:
        ll = line.split(":")
        key = int(ll[0].replace("Game ", ""))

        for g in ll[1].split(";"):
            red_match = red_pattern.search(g)
            green_match = green_pattern.search(g)
            blue_match = blue_pattern.search(g)
            if (red_match and int(red_match.group(1)) > max_dict["red"]) or \
                    (green_match and int(green_match.group(1)) > max_dict["green"]) or \
                    (blue_match and int(blue_match.group(1)) > max_dict["blue"]):
                break
        else:
            total += key
    print(total)

    total = 0
    for line in lines:
        red = 0
        green = 0
        blue = 0
        for g in line.split(":")[1].split(";"):
            red_match = red_pattern.search(g)
            green_match = green_pattern.search(g)
            blue_match = blue_pattern.search(g)
            if red_match:
                red = max(red, int(red_match.group(1)))
            if green_match:
                green = max(green, int(green_match.group(1)))
            if blue_match:
                blue = max(blue, int(blue_match.group(1)))
        total += red * green * blue
    print(total)


if __name__ == "__main__":
    main()
