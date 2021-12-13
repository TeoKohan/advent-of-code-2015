I = [line.strip() for line in open('input')]
A = [[True if c == '#' else False for c in line] for line in I]

n = 100
D = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def neighbours(A, x, y):
    N = [(x+u, y+v) for (u, v) in D if 0 <= x+u < n and 0 <= y+v < n]
    return sum([1 for (u, v) in N if A[v][u]])

def simulate(A):
    B = [[neighbours(A, x, y) for x in range(n)] for y in range(n)]
    B = [[(A[y][x] and B[y][x] in [2, 3]) or (not A[y][x] and B[y][x] == 3) for x in range(n)] for y in range(n)]
    return B

B = A[:]
for i in range(100):
    B = simulate(B)

conway_game_on = sum([1 for row in B for cell in row if cell])

B = A[:]
for i in range(100):
    B = simulate(B)
    B[0][0] = B[0][n-1] = B[n-1][0] = B[n-1][n-1] = True

santas_game_on = sum([1 for row in B for cell in row if cell])

output = open('output', 'w')
output.write(str(conway_game_on) + '\n' + str(santas_game_on) + '\n')
output.close()