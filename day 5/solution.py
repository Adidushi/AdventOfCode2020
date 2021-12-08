def bf_to_num(num):
    total = 0
    for index, char in enumerate(reversed(num)):
        total += 2**index if char == 'B' else 0
    return total

def rl_to_num(num):
    total = 0
    for index, char in enumerate(reversed(num)):
        total += 2**index if char == 'R' else 0
    return total

def seat_id(num):
    row, col = num
    if row * 8 + col == 84:
        print(row, col)
    return row * 8 + col

def q1():
    with open('day 5\input.txt', 'r') as f:
        input = [line.strip() for line in f.readlines()]
    rows = list(line[:7] for line in input)
    rows = list(map(bf_to_num, rows))
    cols = list(line[7:] for line in input)
    cols = list(map(rl_to_num, cols))
    seat_ids = list(map(seat_id, zip(rows, cols)))
    return max(seat_ids)


def q2():
    with open('day 5\input.txt', 'r') as f:
        input = [line.strip() for line in f.readlines()]
    rows = list(line[:7] for line in input)
    rows = list(map(bf_to_num, rows))
    cols = list(line[7:] for line in input)
    cols = list(map(rl_to_num, cols))
    seat_ids = list(map(seat_id, zip(rows, cols)))
    # print(sorted(seat_ids))
    for id in range(min(seat_ids), max(seat_ids)+1):
        if id not in seat_ids:
            return id
    


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
