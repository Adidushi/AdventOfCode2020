from dataclasses import dataclass

@dataclass
class Entry:
    min: int
    max: int
    char: str
    password: str

    def is_valid(self):
        return self.min <= self.password.count(self.char) <= self.max

    def is_valid_2(self):
        try:
            return (self.password[self.min-1] == self.char) + (self.password[self.max-1] == self.char) == 1
        except IndexError:
            return False


def q1():
    with open('day 2\input.txt', 'r') as f:
        input = f.readlines()

    entries = list()

    for entry in input:
        entry, password = entry.split(':')
        entry, char = entry.split()
        min, max = entry.split('-')

        min = int(min)
        max = int(max)
        char = char.strip()
        password = password.strip()

        entries.append(Entry(min, max, char, password).is_valid())

    return sum(entries)
    
def q2():
    with open('day 2\input.txt', 'r') as f:
        input = f.readlines()

    entries = list()

    for entry in input:
        entry, password = entry.split(':')
        entry, char = entry.split()
        min, max = entry.split('-')

        min = int(min)
        max = int(max)
        char = char.strip()
        password = password.strip()

        entries.append(Entry(min, max, char, password).is_valid_2())

    return sum(entries)

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')