from math import prod

I = [line.strip() for line in open('input')]
stats = [[int(n) for n in line.replace(',', ' ').split() if n.lstrip('-').isnumeric()] for line in I]
ingredients = list([line.split()[0].rstrip(':') for line in I])
ingredients = list(zip(ingredients, stats))

def menu(x, y, z, w):
    recipe = list(zip(ingredients, (x, y, z, w)))
    recipe = [[stat * ingredient[1] for stat in ingredient[0][1]] for ingredient in recipe]
    recipe = list(zip(*recipe))
    recipe = [sum(stat) for stat in recipe]
    recipe = [0 if stat < 0 else stat for stat in recipe]
    return recipe

P = [(x, y, z) for x in range(101) for y in range(101-x) for z in range(101-x-y)]
S = [prod(menu(x, y, z, 100-(x+y+z))[:-1]) for (x, y, z) in P]
C = [prod(menu(x, y, z, 100-(x+y+z))[:-1]) * (0 if menu(x, y, z, 100-(x+y+z))[-1] != 500 else 1) for (x, y, z) in P]

output = open('output', 'w')
output.write(str(max(S)) + '\n' + str(max(C)) + '\n')
output.close()