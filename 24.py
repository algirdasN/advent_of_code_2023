class Hailstone:

    def __init__(self, data):
        data = data.split(" @ ")
        self.px, self.py, self.pz = [int(x) for x in data[0].split(", ")]
        self.vx, self.vy, self.vz = [int(x) for x in data[1].split(", ")]

    def intersects_xy(self, other, start, end):
        divisor = self.vy * other.vx - self.vx * other.vy
        if divisor == 0:
            return False

        t1 = (other.vx * (other.py - self.py) + other.vy * (self.px - other.px)) / divisor
        x = self.px + self.vx * t1
        y = self.py + self.vy * t1
        t2 = (x - other.px) / other.vx

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
