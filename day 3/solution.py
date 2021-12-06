class Forest:
    def __init__(self, input):
        self.forest = [[False if char == '.' else True for char in line]
                       for line in input]
        self.height = len(self.forest)
        self.width = len(self.forest[0])

    def get_tile(self, pos):
        x, y = pos
        if x >= self.width:
            x %= self.width
        return self.forest[y][x]


def q1(side, vert):
    with open('day 3\input.txt', 'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]
    forest = Forest(input)
    encounters = list()
    coords = [(side * i, vert * i) for i in range(forest.height//vert)]

    for coord in coords:
        encounters.append(forest.get_tile(coord))
    return sum(encounters)


def q2():
    import math
    pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod([q1(side, vert) for side, vert in pairs])


if __name__ == '__main__':
    print(f'Part 1: {q1(3, 1)}')
    print(f'Part 2: {q2()}')
