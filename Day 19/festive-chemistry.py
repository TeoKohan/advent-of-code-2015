I = [line.strip() for line in open('input')]
L = I[:-2]
F = I[-1]

R = {
    'Al': 'A',
    'Ca': 'C',
    'Mg': 'M',
    'Si': 'S',
    'Th': 'Z',
    'Ti': 'T',
    'Rn': '(',
    'Ar': ')',
    'Y' : '|'
}

def translate(line):
    for (k, v) in R.items():
        line = line.replace(k, v)
    return line

F = translate(F)
L = [translate(line) for line in L]

L = [line.split('=>') for line in L]
L = [[word.strip() for word in line] for line in L]

D = {}
for (k, v) in L:
    if k in D:
        D[k] += [v]
    else:
        D[k]  = [v]

def evolve(F):
    FS = []
    for i in range(len(F)):
        if F[i] in D:
            FS += [F[:i] + v + F[i+1:] for v in D[F[i]]]
    return list(set(FS))

combinations = len(evolve(F))

F = ''.join([c if c in ['(', '|', ')'] else '-' for c in F])

def reduce(F, T):
    T, F = T + F.count('--'),       F.replace('--', '-')
    T, F = T + F.count('-(-)'),     F.replace('-(-)', '-')
    T, F = T + F.count('-(-)'),     F.replace('-(-)', '-')
    T, F = T + F.count('-(-|-)'),   F.replace('-(-|-)', '-')
    T, F = T + F.count('-(-|-|-)'), F.replace('-(-|-|-)', '-')
    return F, T

T = 0
while len(F) > 1:
    F, T = reduce(F, T)
shortest = T

output = open('output', 'w')
output.write(str(combinations) + '\n' + str(shortest) + '\n')
output.close()