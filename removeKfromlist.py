def removeKFromList(s, k):
    return [i for i in s if i != k]
    

seq = [1, 2, 3, 3 ,3 ,4, 4, 5, [5, 6]]

ans = removeKFromList(seq, 3)
