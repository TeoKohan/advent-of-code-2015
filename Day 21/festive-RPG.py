from itertools import chain, combinations
from math import inf
I = [line.strip() for line in open('input')]
(H, D, A) = [int(L.split(':')[1].strip()) for L in I]
boss = {'health': H, 'damage': D, 'armor': A}

weapons = {
    'Dagger'     : ( 8, 4, 0),
    'Shortsword' : (10, 5, 0),
    'Warhammer'  : (25, 6, 0),
    'Longsword'  : (40, 7, 0),
    'Greataxe'   : (74, 8, 0)
}

armor = {
    'Leather'    : ( 13, 0, 1),
    'Chainmail'  : ( 31, 0, 2),
    'Splintmail' : ( 53, 0, 3),
    'Bandedmail' : ( 75, 0, 4),
    'Platemail'  : (102, 0, 5)
}

rings = {
    'Damage  +1' : ( 25, 1, 0),
    'Damage  +2' : ( 50, 2, 0),
    'Damage  +3' : (100, 3, 0),
    'Defense +1' : ( 20, 0, 1),
    'Defense +2' : ( 40, 0, 2),
    'Defense +3' : ( 80, 0, 3)
}

weapon_sets = [[weapons[W] for W in WS] for WS in (combinations(weapons, 1))]
armor_sets = [[armor[A] for A in AS] for AS in chain.from_iterable(combinations(armor, A) for A in range(2))]
aring_sets = [[rings[R] for R in RS] for RS in chain.from_iterable(combinations(rings, R) for R in range(3))]

def equip(items):
    player = {'health': 100, 'damage': 0, 'armor': 0, 'gold': 0}
    for item in items:
        player['gold']   += item[0]
        player['damage'] += item[1]
        player['armor' ] += item[2]
    return player

def damage(atacker, defendant):
    defendant['health'] -= max(1, atacker['damage'] - defendant['armor'])

def fight(player, boss):
    attacker, defender = player, boss
    while player['health'] > 0 and boss['health'] > 0:
        damage(attacker, defender)
        attacker, defender = defender, attacker
    return (player['health'] > 0, player['gold'])

equipment_sets = [(WS, AS, RS) for WS in weapon_sets for AS in armor_sets for RS in aring_sets]
outcomes = [fight(equip([*WS, *AS, *RS]), {} | boss) for (WS, AS, RS) in equipment_sets]

cheapest_victory = min([outcome for outcome in outcomes if outcome[0]])[1]
priciest_loss = max([outcome for outcome in outcomes if not outcome[0]])[1]

output = open('output', 'w')
output.write(str(cheapest_victory) + '\n' + str(priciest_loss) + '\n')
output.close()