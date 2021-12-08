I = [line.strip() for line in open('input')]
L = [[int(n) for n in line.split('x')] for line in I]

S = [sorted([line[0] * line[1], line[0] * line[2], line[1] * line[2]]) for line in L]
S = [line[0] + sum(line) * 2 for line in S]
print(sum(S))

R = [sorted(line) for line in L]
R = [(line[0] + line[1]) * 2 + line[0] * line[1] * line[2] for line in R]
print(sum(R))

output = open('output', 'w')
#output.write(str(final_floor) + '\n' + str(basement) + '\n')
output.close()