import heapq
import sys


class Node:
    def __init__(self, value, x: int, y: int, last_dir: tuple[int, int]):
        self.value = value
        self.x = x
        self.y = y
        self.last_dir = last_dir

        if x == 0 and y == 0:
            self.dist = 0
        else:
            self.dist = sys.maxsize

    def __lt__(self, other):
        return self.dist < other.dist

    def min_dist(self, dist):
        if dist < self.dist:
            self.dist = dist
            return True
        return False


def main():
    with open("data/17.txt") as file:
        grid = file.read().split("\n")

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # prev = {y: [[((0, 0), -1, -1) for _ in range(len(x))] for x in grid] for y in directions}
    node_map = {y: [[(Node(int(grid[i][j]), i, j, y)) for j in range(len(grid[i]))] for i in range(len(grid))] for y in
                directions}

    dist_heap = [node_map[(0, -1)][0][0], node_map[(-1, 0)][0][0]]

    while dist_heap:
        update = False
        node = heapq.heappop(dist_heap)

        for d in directions:
            if d[0] != node.last_dir[0] and d[1] != node.last_dir[1]:
                new_dist = node.dist
                for i in range(1, 4):
                    new_x = node.x + d[0] * i
                    new_y = node.y + d[1] * i
                    if new_x not in range(len(grid)) or new_y not in range(len(grid[0])):
                        break

                    next_node = node_map[d][new_x][new_y]
                    if next_node.dist == sys.maxsize:
                        heapq.heappush(dist_heap, next_node)

                    new_dist += next_node.value
                    if next_node.min_dist(new_dist):
                        update = True
                        # prev[d][new_x][new_y] = (node.last_dir, node.x, node.y)

        if update:
            heapq.heapify(dist_heap)

    print(min(
        node_map[(0, 1)][-1][-1].dist,
        node_map[(1, 0)][-1][-1].dist
    ))


if __name__ == "__main__":
    main()
