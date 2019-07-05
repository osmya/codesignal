def sh(n):
    if n == 0:
         return 0
    elif n == 1:
        return 1
    else:
        return sh(n-1) + 4*(n-1)
    
    
# non recursive
def sh(n):
    return n**2 + (n-1)**2
