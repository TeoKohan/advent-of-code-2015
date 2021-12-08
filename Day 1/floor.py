I = [line.strip() for line in open('input')]
L = I[0]
F = [1 if p == '(' else -1 for p in L]
final_floor = sum(F)
B = [sum(F[0:n]) for n in range(len(F))]
basement = [n for n in range(len(B)) if B[n] < 0][0]

output = open('output', 'w')
output.write(str(final_floor) + '\n' + str(basement) + '\n')
output.close()