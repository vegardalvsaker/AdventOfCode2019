class ContinueI(Exception):
    pass


continue_i = ContinueI()
count = 0
for p in range(147981, 691423+1):
    valid = False
    numbers = [0] * 10
    numbers[int(str(p)[0])] = 1
    try:
        for i, j in enumerate(str(p)):
            if i == 0:
                continue
            d = int(str(p)[i])
            pd = int(str(p)[i-1])
            if d < pd:
                raise continue_i
            numbers[d] += 1
        valid = 2 in numbers

    except ContinueI:
        continue
    if valid:
        count += 1
print(f'Valid passwords: {count}')
