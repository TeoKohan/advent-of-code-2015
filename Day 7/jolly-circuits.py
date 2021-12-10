I = [line.strip() for line in open('input')]
(INS, OUT) = zip(*[line.split('->') for line in I])
OUT = [n.strip() for n in OUT]
INS = [n.split() for n in INS]
I = list(zip(OUT, INS))

result  = { }
signals = { }
for (signal, function) in I:
    signals[signal] = function

functions = {
    'OR'    : lambda x, y: x |  y,
    'AND'   : lambda x, y: x &  y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'NOT'   : lambda x   :     ~x
}

def parse(signal):
    if signal in result:
        return result[signal]
    if signal not in signals:
        result[signal] = int(signal)
    else:
        operation = signals[signal]
        if (len(operation) == 1):
            result[signal] = parse(operation[0])
        if (len(operation) == 2):
            (OP, R) = (functions[operation[0]], parse(operation[1]))
            result[signal] =  OP(R)
        if (len(operation) == 3):
            (L, OP, R) = (parse(operation[0]), functions[operation[1]], parse(operation[2]))
            result[signal] =  OP(L, R)
    return result[signal]

simple_circuit = parse('a')
signals['b'] = [str(simple_circuit)]
result  = { }
modified_circuit = parse('a')

output = open('output', 'w')
output.write(str(simple_circuit) + '\n' + str(modified_circuit) + '\n')
output.close()