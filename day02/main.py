def program(ints):
    for i in range(0, len(ints), 4):
        if ints[i] is 1:
            ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
        elif ints[i] is 2:
            ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
        elif ints[i] is 99:
            return ints[0]


def part1():
    f = open("input.txt", "r")
    for l in f:
        ints = list(map(int, l.split(",")))
        ints[1] = 12
        ints[2] = 2
        print(f'Value at positon 0: {program(ints)}')
    f.close()


def part2():
    f = open("input.txt", "r")
    for t in f:
        for noun in range(0, 100):
            for verb in range(0, 100):
                ints = list(map(int, t.split(",")))
                ints[1] = noun
                ints[2] = verb
                if program(ints) == 19690720:
                    print(f'The answer is {100*noun+verb}')
    f.close()


if __name__ == "__main__":
    part1()
    part2()
