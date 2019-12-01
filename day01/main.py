import math

print(sum([(math.floor((int(n)/3))-2) for n in open("input.txt", "r")]))
