def q1():
    with open('day 8\input.txt', 'r') as f:
        input = f.read().replace('+', '').splitlines()

    input = map(str.split, input)
    input = list(map(lambda l: [l[0], int(l[1])], input))

    visited = set()

    acc = 0
    curr_line = 0

    while curr_line < len(input):
        if curr_line in visited:
            return acc
        visited.add(curr_line)
        op, num = input[curr_line]
        if op == 'nop':
            curr_line += 1
            continue
        if op == 'acc':
            acc += num
            curr_line += 1
            continue
        if op == 'jmp':
            curr_line += num
            continue
    return acc


def run(input):
    visited = set()

    acc = 0
    curr_line = 0

    while curr_line < len(input):
        if curr_line in visited:
            return None
        visited.add(curr_line)
        op, num = input[curr_line]
        if op == 'nop':
            curr_line += 1
            continue
        if op == 'acc':
            acc += num
            curr_line += 1
            continue
        if op == 'jmp':
            curr_line += num
            continue
    return acc


def q2():
    with open('day 8\input.txt', 'r') as f:
        input = f.read().replace('+', '').splitlines()

    input = map(str.split, input)
    input = list(map(lambda l: [l[0], int(l[1])], input))

    for line_num in range(len(input)):
        orig = input[line_num][0]

        new_cmd = 'jmp' if orig == 'nop' else 'nop'
        input[line_num][0] = new_cmd

        sample_run = run(input)
        if sample_run is not None:
            return sample_run

        input[line_num][0] = orig


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
