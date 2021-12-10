I = [line.strip() for line in open('input')]
L = [line.split() for line in I]
L = [[word for word in line if word != 'turn' and word != 'through'] for line in L]
[A, L, R] = list(zip(*L))

L = [line.split(',') for line in L]
L = [[int(n) for n in line] for line in L]
R = [line.split(',') for line in R]
R = [[int(n) for n in line] for line in R]

S = list(zip(L, R))
S = [(range(u, w+1), range(v, z+1)) for [(u, v), (w, z)] in S]
O = [(A[i], S[i]) for i in range(len(I))]

common_nordic_elvish = {
    'on'    : lambda x: 1,
    'off'   : lambda x: 0,
    'toggle': lambda x: 1 if x == 0 else 0
}

ancient_nordic_elvish = {
    'on'    : lambda x: x+1,
    'off'   : lambda x: max(0, x-1),
    'toggle': lambda x: x+2
}

def light_show(translation, instructions):
    H = [[0 for x in range(1000)] for y in range(1000)] 

    for (action, (X, Y)) in instructions:
        for (x, y) in [(x, y) for x in X for y in Y]:
            H[y][x] = translation[action](H[y][x])
    H = [cell for row in H for cell in row]
    return sum(H)

output = open('output', 'w')
output.write(str(light_show(common_nordic_elvish, O)) + '\n' + str(light_show(ancient_nordic_elvish, O)) + '\n')
output.close()