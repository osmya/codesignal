def isCryptSolution(c, s):
    keys = {key: value for (key, value) in s}
    factors = []
    total = []
    
    for i in c[:-1]: # penultimate so it excludes total
        for j in range(len(i)):
            if i[j] in keys:
                if len(i) > 1 and keys[i[0]] == '0':
                    return False
                factors += keys[i[j]]
                
    for i in c[-1]: # j is the key so get the value
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
