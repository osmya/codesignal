def adjacentElementsProduct(a):
    k = [x*y for x, y in zip(a[1:], a)]
    return max(k)

# cleaner

def adjacentElementsProduct(a):
    return max([x*y for x, y in zip(a[1:], a)])
    
# or directly max(x*y for x, y in zip(a[1:], a))


# other approach

def adjacentElementsProduct(a):
    return max([a[i] * a[i+1] for i in range(len(a)-1)])



