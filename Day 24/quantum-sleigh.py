from math import prod, inf
from itertools import chain, combinations

I = [int(line.strip()) for line in open('input')]
third   = sum(I) // 3
quarter = sum(I) // 4

def powerset(iterable, R):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in R)

def quantum(A):
    return prod(A)

def split_thirds(I, S, Q):
    A = next((x for x in powerset(I, range(S+1)) if sum(x) == third and quantum(x) < Q), None)
    P = [x for x in I if x not in A]
    B = next((x for x in powerset(P, range(len(P)+1)) if sum(x) == third), None)
    C = [x for x in P if x not in B]
    return(A, B, C)

def split_quarters(I, S, Q):
    A = next((x for x in powerset(I, range(S+1)) if sum(x) == quarter and quantum(x) < Q), None)
    P = [x for x in I if x not in A]
    B = next((x for x in powerset(P, range(len(P)+1)) if sum(x) == quarter), None)
    P = [x for x in P if x not in B]
    C = next((x for x in powerset(P, range(len(P)+1)) if sum(x) == quarter), None)
    D = [x for x in P if x not in C]
    return(A, B, C, D)

(A, B, C) = split_thirds(I, len(I), inf)
smallest_third = quantum(min(A, B, C, key = lambda x: len(x)))

(A, B, C, D) = split_quarters(I, len(I), inf)
smallest_quarter = quantum(min(A, B, C, D, key = lambda x: len(x)))

output = open('output', 'w')
output.write(str(smallest_third) + '\n' + str(smallest_quarter) + '\n')
output.close()