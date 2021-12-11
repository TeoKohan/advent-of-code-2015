from itertools import permutations

I = [line.strip() for line in open('input')]

guests = list(set([line.split()[0] for line in I]))
guests = { i: guests[i] for i in range(len(guests)) }
mood = { (L.split()[0], L.split()[-1][:-1]): [int(n) for n in L.split() if n.isnumeric()][0] * (-1 if 'lose' in L else 1) for L in I}

def calculate_happiness(L):
    total_happiness = 0
    for guest in range(len(L)):
        left  = L[guest - 1]
        center= L[guest]
        right = L[(guest + 1) % len(L)]
        (left, center, right) = [guests[n] for n in (left, center, right)]
        (left, right) = (mood[(center, left)], mood[(center, right)])
        total_happiness += left + right
    return total_happiness

P = [[0] + list(p) for p in permutations(range(1, len(guests)))]
D = [calculate_happiness(C) for C in P]

maximum_happiness = max(D)

guests[len(guests)] = 'Me' 
mood = mood | { ('Me', guest): 0 for guest in guests.values()}
mood = mood | { (guest, 'Me'): 0 for guest in guests.values()}

P = [[0] + list(p) for p in permutations(range(1, len(guests)))]
D = [calculate_happiness(C) for C in P]

maximum_british_happiness = max(D)

output = open('output', 'w')
output.write(str(maximum_happiness) + '\n' + str(maximum_british_happiness) + '\n')
output.close()
