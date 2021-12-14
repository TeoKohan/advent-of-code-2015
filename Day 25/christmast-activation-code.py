from itertools import islice

I = [line.strip() for line in open('input')]
L = I[0].split()[-4:]
(row, column) = (int(L[1].strip(',')), int(L[-1].strip('.')))

start = 20151125

def codes():
    n = 20151125
    while True:
        yield n
        n = (n * 252533) % 33554393

diagonal = row+column
code_index = diagonal * (diagonal-1) // 2 - row
code = list(islice(codes(), code_index, code_index+1))[0]

output = open('output', 'w')
output.write(str(code) + '\n')
output.close()