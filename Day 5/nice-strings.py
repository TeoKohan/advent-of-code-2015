I = [line.strip() for line in open('input')]

def vowels(line):
    V = [c for c in line if c in ['a', 'e', 'i', 'o', 'u']]
    return len(V) > 2

def twice(line):
    T = [line[i] for i in range(1, len(line)) if line[i] == line[i-1]]
    return len(T) > 0

def naughty(line):
    for i in range(len(line)-1):
        if (line[i:i+2] in ['ab', 'cd', 'pq', 'xy']):
            return True
    return False

N = [line for line in I if vowels(line) and twice(line) and not naughty(line)]

first_draft = len(N)

def two_substring(line):
    for i in range(len(line)-1):
        ss = line[i:i+2]
        for j in range(i+2, len(line)-1):
            if (ss == line[j:j+2]):
                return True
    return False

def split_repeat(line):
    for i in range(len(line)-2):
        if (line[i:i+3][0] == line[i:i+3][2]):
            return True
    return False

N = [line for line in I if two_substring(line) and split_repeat(line)]

second_draft = len(N)

output = open('output', 'w')
output.write(str(first_draft) + '\n' + str(second_draft) + '\n')
output.close()