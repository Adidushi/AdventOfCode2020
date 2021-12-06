def q1():
    with open('day 1\input.txt', 'r') as f:
        input = f.readlines()

    input = [int(num.strip()) for num in input]

    for num1 in input:
        for num2 in input:
            if num1 + num2 == 2020:
                return num1 * num2

    print(input)
    
def q2():
    with open('day 1\input.txt', 'r') as f:
        input = f.readlines()

    input = [int(num.strip()) for num in input]

    for num1 in input:
        for num2 in input:
            for num3 in input:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')