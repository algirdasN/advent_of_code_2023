import re
from copy import copy


class Part:
    _pattern = re.compile(r"(\d+)")

    def __init__(self, string):
        matches = Part._pattern.findall(string)
        self.x = int(matches[0])
        self.m = int(matches[1])
        self.a = int(matches[2])
        self.s = int(matches[3])

    def value(self):
        return self.x + self.m + self.a + self.s


class TheoreticPart:
    def __init__(self, x=range(1, 4001), m=range(1, 4001), a=range(1, 4001), s=range(1, 4001)):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def possible(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)


class Workflow:
    _pattern = re.compile(r"([^{},]+)")

    def __init__(self, string, workflows):
        self.instructions = Workflow._pattern.findall(string)
        self.workflows = workflows

    def apply(self, part: Part):
        for i in self.instructions:
            x = i.split(":")
            if len(x) == 1 or eval("part." + x[0]):
                return x[-1] if x[-1] in ("A", "R") else self.workflows[x[-1]].apply(part)

    def apply_theory(self, part: TheoreticPart):
        if part.possible() == 0:
            return []

        valid_parts = []

        for i in self.instructions:
            x = i.split(":")

            if len(x) == 1:
                break

            v = int(x[0][2:])
            r = getattr(part, x[0][0])

            if ("<" in x[0] and r.stop <= v) or (">" in x[0] and r.start > v):
                break

            if v not in r:
                continue

            new_part = copy(part)
            if "<" in x[0]:
                setattr(part, x[0][0], range(v, r.stop))
                setattr(new_part, x[0][0], range(r.start, v))
            else:
                setattr(part, x[0][0], range(r.start, v + 1))
                setattr(new_part, x[0][0], range(v + 1, r.stop))
            valid_parts.extend(self.apply_theory(new_part))

        valid_parts.extend([part] if x[-1] == "A"
                           else [] if x[-1] == "R" else self.workflows[x[-1]].apply_theory(part))

        return valid_parts


def main():
    with open("data/19.txt") as file:
        w, p = file.read().split("\n\n")

    workflows = {}
    for i in w.split("\n"):
        x = i.index("{")
        workflows[i[:x]] = Workflow(i[x:], workflows)

    parts = [Part(x) for x in p.split("\n")]

    print(sum(p.value() for p in parts if workflows["in"].apply(p) == "A"))

    possible_parts = workflows["in"].apply_theory(TheoreticPart())

    print(sum(x.possible() for x in possible_parts))


if __name__ == "__main__":
    main()
