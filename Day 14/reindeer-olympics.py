I = [line.strip() for line in open('input')]
stats = [[int(n) for n in line.split() if n.isnumeric()] for line in I]
reindeers = list([line.split()[0] for line in I])
reindeers = list(zip(reindeers, stats))
reindeers = { reindeer: {'speed': speed, 'stamina': stamina, 'recovery': recovery} for (reindeer, (speed, stamina, recovery)) in reindeers }

def simulate_reindeer(reindeer):
    if reindeer['tiredness'] > 0:
        reindeer['tiredness']-=1
    elif reindeer['energy'] == 1:
        reindeer['position'] += reindeer['speed']
        reindeer['energy'] = reindeer['stamina']
        reindeer['tiredness'] = reindeer['recovery']
    else:
        reindeer['position'] += reindeer['speed']
        reindeer['energy'] -= 1

R = [reindeer | {'position': 0, 'energy': reindeer['stamina'], 'tiredness': 0} for reindeer in reindeers.values()]

for i in range(2503):
    for reindeer in R:
        simulate_reindeer(reindeer)
furthest = max(R, key = lambda r: r['position'])['position']

R = [reindeer | {'position': 0, 'energy': reindeer['stamina'], 'tiredness': 0, 'points': 0} for reindeer in reindeers.values()]

for i in range(2503):
    for reindeer in R:
        simulate_reindeer(reindeer)
    leader = max(R, key = lambda r: r['position'])
    leader['points'] += 1
winner = max(R, key = lambda r: r['points'])['points']

output = open('output', 'w')
output.write(str(furthest) + '\n' + str(winner) + '\n')
output.close()