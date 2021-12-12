from functools import reduce

I = [line.strip() for line in open('input')]
I = [int(line) for line in I]

def fill_container(remaining, capacity):
    return [remaining] + ([(remaining[0] - capacity, remaining[1] + 1)] if remaining[0] - capacity >= 0 else [])

def fill_containers (CS, capacity):
    return [c for C in CS for c in fill_container(C, capacity)]

C = reduce(fill_containers, I, [(150, 0)])
Z = [(v, q) for (v, q) in C if v == 0]

M = [(v, q) for (v, q) in Z if q == min(Z, key = lambda t: t[1])[1]]

output = open('output', 'w')
output.write(str(len(Z)) + '\n' + str(len(M)) + '\n')
output.close()