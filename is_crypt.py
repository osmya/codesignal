def isCryptSolution(c, s):
    keys = {key: value for (key, value) in s} # can use dict(s)
    factors = []
    total = []
    
    for i in c[:-1]: # penultimate so it excludes total
        for j in range(len(i)):
            if i[j] in keys:
                if len(i) > 1 and keys[i[0]] == '0':
                    return False
                factors += keys[i[j]]
                
    for i in c[-1]: # the last value
        for j in range(len(i)):
            if i[j] in keys:
                if len(i) > 1 and keys[i[0]] == '0':
                    return False
                total += keys[i[j]]
                
    if len(total) > 1 and total[0] == '0':
        return False
    t = int(''.join(total))
    f = [''.join(factors[i:i+len(c[0])]) for i in range(0, len(factors), len(c[0]))]
    h = [int(f[i]) for i in range(len(f))]
    return sum(h) == t


# brilliant solution that maps each word to a num via convert helper func

def is_crypt(crypt, solution):
    d = dict(solution)
    
    def convert(c):
        return d[c]
    decoded = list()
    
    for word in crypt:
        num = ''.join([convert(c) for c in word])
        if num[0] == '0' and len(num) > 1:
            return False
        decoded.append(int(num))

    return decoded[0] + decoded[1] == decoded[2]
