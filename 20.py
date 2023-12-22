from collections import deque


class Module:
    def __init__(self, modules, name, destinations):
        self.modules = modules
        self.name = name
        self.destinations = destinations.split(", ")
        self.last_input = {}

    def update_inputs(self):
        for d in self.destinations:
            mod = self.modules.get(d)
            if mod:
                mod.last_input[self.name] = False

    def receive(self, input_name, pulse):
        raise Exception()


signals: deque[tuple[Module, str, bool]] = deque()
low_count = 0
high_count = 0


class Broadcaster(Module):
    def receive(self, input_name, pulse):
        global low_count, high_count

        for d in self.destinations:
            signals.append((self.modules.get(d), self.name, pulse))
            if pulse:
                high_count += 1
            else:
                low_count += 1


class FlipFlop(Module):

    def __init__(self, modules, name, destinations):
        super().__init__(modules, name, destinations)
        self.state = False

    def receive(self, input_name, pulse):
        global low_count, high_count

        if pulse:
            return

        self.state = not self.state
        for d in self.destinations:
            signals.append((self.modules.get(d), self.name, self.state))
            if self.state:
                high_count += 1
            else:
                low_count += 1


class Conjunction(Module):
    def __init__(self, modules, name, destinations):
        super().__init__(modules, name, destinations)

    def receive(self, input_name, pulse):
        global low_count, high_count

        self.last_input[input_name] = pulse

        out = not all(self.last_input.values())
        for d in self.destinations:
            signals.append((self.modules.get(d), self.name, out))
            if out:
                high_count += 1
            else:
                low_count += 1


def main():
    global low_count, high_count

    with open("data/20.txt") as file:
        lines = file.read().split("\n")

    modules: dict[str, Module] = {}

    for line in lines:
        x = line.split(" -> ")
        if x[0] == "broadcaster":
            modules["broadcaster"] = Broadcaster(modules, "broadcaster", x[1])
        elif x[0][0] == "%":
            modules[x[0][1:]] = FlipFlop(modules, x[0][1:], x[1])
        elif x[0][0] == "&":
            modules[x[0][1:]] = Conjunction(modules, x[0][1:], x[1])
        else:
            raise Exception()

    for m in modules.values():
        m.update_inputs()

    for i in range(1000):
        low_count += 1
        modules["broadcaster"].receive(None, False)
        while signals:
            mod, name, pulse = signals.popleft()
            if mod:
                mod.receive(name, pulse)

    print(low_count * high_count)


if __name__ == "__main__":
    main()
