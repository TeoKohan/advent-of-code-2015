I = [line.strip() for line in open('input')]
I = [line.split() for line in I]
I = [[word for word in line if word != 'to' and word != '='] for line in I]

locations = list(set([word for line in I for word in line if not word.isnumeric()]))
locations = { locations[i]: i for i in range(len(locations)) }
distances = { (min(locations[a], locations[b]), max(locations[a], locations[b])): int(d) for (a, b, d) in I }

def calculate_path(L):
    D = [distances[(min(L[i], L[i+1]), max(L[i], L[i+1]))] for i in range(len(L)-1)]
    return sum(D)

def permutations(A, P = []):
    AA = []
    for e in A:
        B = A[:]
        B.remove(e)
        Q = P[:]
        Q += [e]
        if B == []:
            AA += [Q]
        else:
            AA += permutations(B, Q)
    return AA

P = permutations(list(range(len(locations))))
D = [calculate_path(C) for C in P]

output = open('output', 'w')
output.write(str(min(D)) + '\n' + str(max(D)) + '\n')
output.close()
