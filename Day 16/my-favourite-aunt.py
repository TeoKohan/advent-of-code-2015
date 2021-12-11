I = [line.strip() for line in open('input')]
Sues = ["".join(line.split()[2:]) for line in I]
Sues = [Sue.split(',') for Sue in Sues]
Sues = {n+1: {stat.split(':')[0]: int(stat.split(':')[1]) for stat in Sues[n]} for n in range(len(Sues))}

my_favourite_Sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def my_Sue(Sue):
    for stat in my_favourite_Sue.keys():
        if stat in Sue and my_favourite_Sue[stat] != Sue[stat]:
            return False
    return True

def my_true_Sue(Sue):
    for stat in my_favourite_Sue.keys():
        if stat in Sue:
            if stat in ['cats', 'trees'] and my_favourite_Sue[stat] >= Sue[stat]:
                return False
            if stat in ['pomeranians', 'goldfish'] and my_favourite_Sue[stat] <= Sue[stat]:
                return False
            if stat not in ['cats', 'trees', 'pomeranians', 'goldfish'] and my_favourite_Sue[stat] != Sue[stat]:
                return False
    return True

aunt_Sue = next(Sue for Sue in Sues if my_Sue(Sues[Sue]))
true_aunt_Sue = next(Sue for Sue in Sues if my_true_Sue(Sues[Sue]))

output = open('output', 'w')
output.write(str(aunt_Sue) + '\n' + str(true_aunt_Sue) + '\n')
output.close()