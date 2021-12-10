I = [line.strip() for line in open('input')]

U = [line[1:-1] for line in I]
U = [line.replace('\\', '|') for line in U]
U = [line.replace('||', 'B') for line in U]
U = [line.replace('|"', 'A') for line in U]
U = [line.replace('|x', 'H') for line in U]

E = [line.replace('B', '||||') for line in U]
E = [line.replace('A', '||||') for line in E]
E = [line.replace('H', '|||') for line in E]

character_number = sum([len(line) for line in I])
decode_number    = sum([len(line) - line.count('H') * 2 for line in U])
encode_number    = sum([len(line) + 6 for line in E])

output = open('output', 'w')
output.write(str(character_number - decode_number) + '\n' + str(encode_number - character_number) + '\n')
output.close()