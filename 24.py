class Hailstone:

    def __init__(self, data):
        data = data.split(" @ ")
        self.px, self.py, self.pz = [int(x) for x in data[0].split(", ")]
        self.vx, self.vy, self.vz = [int(x) for x in data[1].split(", ")]

        self.hn = [self.vy, -self.vx, self.py * self.vx - self.px * self.vy]

    def intersects_xy(self, other, start, end):
        prod = [
            self.hn[1] * other.hn[2] - other.hn[1] * self.hn[2],
            other.hn[0] * self.hn[2] - self.hn[0] * other.hn[2],
            self.hn[0] * other.hn[1] - other.hn[0] * self.hn[1]
        ]

        if prod[2] == 0:
            return False

        x = prod[0] / prod[2]
        y = prod[1] / prod[2]

        try:
            t1 = (x - self.px) / self.vx
        except ZeroDivisionError:
            t1 = (y - self.py) / self.vy

        try:
            t2 = (x - other.px) / other.vx
        except ZeroDivisionError:
            t2 = (y - other.py) / other.vy

        return t1 > 0 and t2 > 0 and start <= x <= end and start <= y <= end


def main():
    with open("data/24.txt") as file:
        grid = file.read().split("\n")

    hail = [Hailstone(x) for x in grid]

    count = 0
    for i in range(len(hail)):
        for j in range(i + 1, len(hail)):
            if hail[i].intersects_xy(hail[j], 200000000000000, 400000000000000):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
