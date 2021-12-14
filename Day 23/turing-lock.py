I = [line.strip() for line in open('input')]

A = {
    'ip': 0,
    'a' : 0,
    'b' : 0
}

def nop(x):
    return x

def hlf(x):
    A[x] //= 2

def tpl(x):
    A[x] *= 3

def inc(x):
    A[x] += 1

def jmp_generic(p, x):
    if p:
        s, n = x[0], int(x[1:])
        A['ip'] = A['ip'] + n - 1 if s == '+' else A['ip'] - n - 1

def jmp(x):
    jmp_generic(True, x)

def jie(x, y):
    jmp_generic(A[x] % 2 == 0, y)

def jio(x, y):
    jmp_generic(A[x] == 1, y)

D = {
    'nop': nop,
    'hlf': hlf,
    'tpl': tpl,
    'inc': inc,
    'jmp': jmp,
    'jie': jie,
    'jio': jio
}

def parse_line(n):
    if n < len(I):
        L = I[n]
        op  = L.split()[0]
        arg = L.split()[1:]
        if len(arg) == 1:
            D[op](arg[0])
        else:
            D[op](arg[0].strip(','), arg[1])
        return True
    return False

def execute():
    while parse_line(A['ip']):
        A['ip'] += 1

execute()
b_0 = A['b']

A = {
    'ip': 0,
    'a' : 1,
    'b' : 0
}
execute()
b_1 = A['b']

output = open('output', 'w')
output.write(str(b_0) + '\n' + str(b_1) + '\n')
output.close()