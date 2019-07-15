def allLongestStrings(a):
    mark = max([len(i) for i in a])
    return [i for i in a if len(i) == mark]


# with map and filter
def allLongestStrings(a):
    m = max(map(len, a))
    return filter(lambda x: len(x) == m, a)
