def q1():
    with open('day 6\input.txt', 'r') as f:
        input = f.read()
    
    groups = [group.replace('\n', '') for group in input.split('\n\n')]

    char_amounts = [len(set(group)) for group in groups]
    return sum(len(set(group)) for group in groups)
    
def q2():
    with open('day 6\input.txt', 'r') as f:
        input = f.read()
    
    groups = [group.split('\n') for group in input.split('\n\n')]

    counter = 0
    for group in groups:
        for question in 'qwertyuiopasdfghjklzxcvbnm':
            if all(question in person for person in group):
                counter += 1

    return counter

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')