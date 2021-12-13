from math import ceil, sqrt, prod
from itertools import chain, combinations

L = [int(line.strip()) for line in open('input')][0]

def factorize(house):
    for i in range(2, ceil(sqrt(house))+1):
        if house % i == 0:
            return [i] + factorize(house // i)
    return [house]

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def presents(house):
    F = [1] + factorize(house)
    elves = sum(set([prod(P) for P in powerset(F)]))
    return 10 * elves

P = 1
while presents(P) < L:
    P += 1
lucky_house = P

def lazy_presents(house):
    F = [1] + factorize(house)
    S = set([prod(P) for P in powerset(F)])
    S = [s for s in S if ((house - s) // s) <= 50]
    elves = sum(S)
    return 11 * elves

P = 1
while lazy_presents(P) < L:
    P += 1
other_lucky_house = P

output = open('output', 'w')
output.write(str(lucky_house) + '\n' + str(other_lucky_house) + '\n')
output.close()