I = [line.strip() for line in open('input')]
L = I[0]

dictionary = {
    '^': lambda x, y: (x,   y+1),
    '>': lambda x, y: (x+1, y),
    'v': lambda x, y: (x,   y-1),
    '<': lambda x, y: (x-1, y)
}

def walk(P):
    position = (0, 0)
    S = set([position])

    for d in P:
        position = dictionary[d](position[0], position[1])
        S.add(position)
    return S

SS = [L[n] for n in range(len(L)) if n % 2 == 0]
RS = [L[n] for n in range(len(L)) if n % 2 == 1]
H = walk(SS).union(walk(RS))

output = open('output', 'w')
output.write(str(len(walk(L))) + '\n' + str(len(H)) + '\n')
output.close()