import copy
from math import inf

I = [line.strip() for line in open('input')]
(H, D) = [int(L.split(':')[1].strip()) for L in I]
boss = {'health': H, 'damage': D, 'armor': 0}

def magic_missile(fight):
    fight['boss']['health'] -= 4

def drain(fight):
    fight['boss']['health'] -= 2
    fight['player']['health'] += 2

def shield(fight):
    fight['effects']['shield'] = 6

def poison(fight):
    fight['effects']['poison'] = 6

def recharge(fight):
    fight['effects']['recharge'] = 5

spells = {
    'magic_missile': (53, magic_missile),
    'drain': (73, drain),
    'shield': (113, shield),
    'poison': (173, poison),
    'recharge': (229, recharge)
}

def cast_spell(cost, spell, fight):
    fight['player']['mana']        -= cost
    fight['info']['mana_spent']    += cost
    fight['info']['active_player'] = 'boss'
    spell(fight)

fight = {
    'player':  {'health': 50, 'mana': 500, 'armor': 0},
    'boss':    {'health': H, 'damage': D, 'armor': 0},
    'effects': {'shield': 0, 'poison': 0, 'recharge': 0},
    'info':    {'mana_spent': 0, 'active_player': 'player', 'hard': False}
}

def advance_timelines(timelines):
    def split_timeline(T):
        return {k: {kv: vv for (kv, vv) in v.items()} for (k, v) in T.items()}
    new_timelines = []
    for T in timelines:
        #Apply effects
        T['player']['armor'] = (7 if T['effects']['shield']     > 0 else 0)
        T['boss']['health'] -= (3 if T['effects']['poison']     > 0 else 0)
        T['player']['mana'] += (101 if T['effects']['recharge'] > 0 else 0)
        T['player']['health'] -= (1 if T['info']['active_player'] == 'player' and T['info']['hard'] else 0)
        T['effects'] = {k: max(0, v-1) for (k, v) in T['effects'].items() }
        #Check end condition
        if T['player']['health'] <= 0 or T['boss']['health'] <= 0:
            new_timelines.append(T)
            continue
        if T['info']['active_player'] == 'player':
            #Split timelines
            for (name, (cost, spell)) in spells.items():
                if T['player']['mana'] >= cost and (name not in T['effects'] or T['effects'][name] == 0):
                    NT = split_timeline(T)
                    cast_spell(cost, spell, NT)
                    new_timelines.append(NT)
        else:
            T['player']['health'] -= max(1, T['boss']['damage'] - T['player']['armor'])
            T['info']['active_player'] = 'player'
            new_timelines.append(T)
    
    return new_timelines

def battle(fight):
    timelines = [{} | fight]
    least_mana_used = inf
    while(len(timelines) > 0 and len(timelines) < 3 * 10**6):
        least_mana_used = min(least_mana_used, min([T['info']['mana_spent'] for T in timelines if T['boss']['health'] <= 0], default = inf))
        timelines = advance_timelines([T for T in timelines if T['info']['mana_spent'] < least_mana_used and T['player']['health'] > 0 and T['boss']['health'] > 0])
    return least_mana_used

normal_fight = battle(fight)

fight['info']['hard'] = True

hard_fight = battle(fight)

output = open('output', 'w')
output.write(str(normal_fight) + '\n' + str(hard_fight) + '\n')
output.close()