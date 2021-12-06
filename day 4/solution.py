def check_height(hgt):
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    return False


def q1():
    with open('day 4\input.txt', 'r') as f:
        input = f.read()

    entries = [entry.replace('\n', ' ').split()
               for entry in input.split('\n\n')]
    entries = [{value.split(':')[0]: value.split(':')[1]
                for value in entry} for entry in entries]

    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return sum([all(k in entry for k in required_fields) for entry in entries])


def q2():
    with open('day 4\input.txt', 'r') as f:
        input = f.read()

    entries = [entry.replace('\n', ' ').split()
               for entry in input.split('\n\n')]
    entries = [{value.split(':')[0]: value.split(':')[1]
                for value in entry} for entry in entries]

    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    char_list = '0123456789abcdef'
    eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    counter = 0
    for entry in entries:
        if not all(k in entry for k in required_fields):
            continue
        if not 1920 <= int(entry.get('byr')) <= 2002:
            continue
        if not 2010 <= int(entry.get('iyr')) <= 2020:
            continue
        if not 2020 <= int(entry.get('eyr')) <= 2030:
            continue
        if not check_height(entry.get('hgt')):
            continue
        if not (entry.get('hcl')[0] == '#' and all([characters in char_list for characters in entry.get('hcl')[1:]])):
            continue
        if not entry.get('ecl') in eye_colors:
            continue
        if not (len(entry.get('pid')) == 9 and entry.get('pid').isnumeric()):
            continue
        counter += 1
    return counter


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
