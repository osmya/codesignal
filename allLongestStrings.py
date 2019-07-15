def allLongestStrings(a):
    mark = max([len(i) for i in a])
    return [i for i in a if len(i) == mark]
