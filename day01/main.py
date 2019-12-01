import math

# one liner part 1
#print(sum([(math.floor((int(n)/3))-2) for n in open("input.txt", "r")]))


def part1():
    f = open("input.txt", "r")
    print(sum([(math.floor((int(n)/3))-2) for n in f]))
    f.close()


def part2():
    f = open("input.txt", "r")
    fuel = 0
    for n in f:
        fuel = fuel + recurse(int(n))
    f.close()
    print(f'Part2: Sum of fuel requirements: {fuel}')


def recurse(fuel):
    required = (math.floor((fuel / 3))-2)
    if required > 0:
        return required + recurse(required)
    else:
        return 0


if __name__ == '__main__':
    part1()
    part2()
