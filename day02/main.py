f = open("input.txt", "r")
for l in f:
    ints = list(map(int, l.split(",")))
    ints[1] = 12
    ints[2] = 2
    for i in range(0, len(ints), 4):
        if ints[i] is 1:
            ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
        elif ints[i] is 2:
            ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
        elif ints[i] is 99:
            print("Program halted")
            break
    print(f'Value at positon 0: {ints[0]}')
f.close()
