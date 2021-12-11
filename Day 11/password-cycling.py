from itertools import groupby
I = [line.strip() for line in open('input')]
L = I[0]

def increment(L, n = 1):
    (P, C, Q) = (L[:-n], L[-n], L[-n:][1:])
    if C == 'z':
        return increment(P+'a'+Q, n+1)
    else:
        return P + chr(ord(C)+1) + Q

def increasing_run(L):
    increasing = [L[n:n+3] for n in range(len(L)-2) if ord(L[n])+1 == ord(L[n+1]) == ord(L[n+2])-1]
    return len(increasing) > 0

def legal_characters(L):
    F = [c for c in L if c in ['i', 'o', 'l']]
    return F == []

def pairs(L):
    P = [list(g) for k,g in groupby(L)]
    if sum([len(S)//2 for S in P]) > 1:
        return True
    return False

while not (increasing_run(L) and legal_characters(L) and pairs(L)):
    L = increment(L)

first_password = L

L = increment(L)
while not (increasing_run(L) and legal_characters(L) and pairs(L)):
    L = increment(L)

second_password = L

output = open('output', 'w')
output.write(str(first_password) + '\n' + str(second_password) + '\n')
output.close()