def contains_bag(wanted_color, current_color, translation_dict):
    if not translation_dict.get(current_color):
        return 0
    if wanted_color in translation_dict[current_color]:
        return 1
    return any(map(lambda c: contains_bag(wanted_color, c, translation_dict), translation_dict[current_color]))


def count_bags(current_color, translation_dict):
    sub_bags = translation_dict.get(current_color)

    if not sub_bags:
        return 1

    multiplied_bags = list()

    for bag in sub_bags:
        amt, color = int(bag.split()[0]), ' '.join(bag.split()[1:])
        for _ in range(amt):
            multiplied_bags.append(color)

    sub_bags = multiplied_bags

    return 1 + sum(map(lambda c: count_bags(c, translation_dict), sub_bags))


def q1():
    with open('day 7\input.txt', 'r') as f:
        input = f.read().splitlines()

    for c in '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'bags', 'bag', ' .':
        input = [line.replace(c, '').strip() for line in input]

    input = [line.split('contain') for line in input]
    input = [[big.strip(), list(map(str.strip, smalls.split(' , ')))]
             for big, smalls in input]

    bag_colors = [line[0] for line in input]

    in_dict = {k: (v if v != ['no other'] else None) for k, v in input}
    return sum(map(lambda c: contains_bag('shiny gold', c, in_dict), bag_colors))


def q2():
    with open('day 7\input.txt', 'r') as f:
        input = f.read().splitlines()
        
    for c in 'bags', 'bag', ' .':
        input = [line.replace(c, '').strip() for line in input]

    input = [line.split('contain') for line in input]
    input = [[big.strip(), list(map(str.strip, smalls.split(' , ')))]
             for big, smalls in input]

    in_dict = {k: (v if v != ['no other'] else None) for k, v in input}
    print(in_dict)
    return count_bags('shiny gold', in_dict)-1


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
