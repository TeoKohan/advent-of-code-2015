import hashlib
I = [line.strip() for line in open('input')]
L = I[0]

def zero_hash(L, n):
    i = 0
    hash = hashlib.md5((L+str(i)).encode())
    while not str(hash.hexdigest())[0:n] == '0' * n:
        i += 1
        hash = hashlib.md5((L+str(i)).encode())
        
    return i

output = open('output', 'w')
output.write(str(zero_hash(L, 5)) + '\n' + str(zero_hash(L, 6)) + '\n')
output.close()