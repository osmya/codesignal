def isLucky(n):
    nl = [int(i) for i in str(n)]
    mid = int(len(nl) / 2)
    return sum(nl[0:mid]) == sum(nl[mid::])
    
    
# alt

def isLucky(n):
    d = map(int, str(n))
    m = len(d) / 2
    return sum(d[:m]) == sum(d[m:])
