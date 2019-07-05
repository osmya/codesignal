def adjacentElementsProduct(a):
    k = [x*y for x, y in zip(a[1:], a)]
    return max(k)

# can do

def adjacentElementsProduct(a):
    return max([x*y for x, y in zip(a[1:], a)])
    
# or directly max(x*y for x, y in zip(a[1:], a))




