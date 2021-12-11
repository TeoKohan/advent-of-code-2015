from itertools import count, groupby
import json 

I = [line.strip() for line in open('input')]
J = json.loads(str(I[0]))

def add_numbers(C, F = None):
    if type(C) is int:
        return C
    if type(C) is str:
        return 0
    if type(C) is dict:
        if F in C.values():
            return 0
        C = C.values()
    return sum([add_numbers(V, F) for V in C])
    
output = open('output', 'w')
output.write(str(add_numbers(J)) + '\n' + str(add_numbers(J, 'red')) + '\n')
output.close()