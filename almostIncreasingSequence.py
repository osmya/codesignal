def almostIncreasingSequence(sequence):
    for i, x in enumerate(sequence):    
        s = sequence[:i]
        s.extend(sequence[i+1:])
        if s == sorted(set(s)):
            return True
    return False

"""
def almostIncreasingSequence(sequence):

    def is_increasing(lst):
        for idx in range(len(lst)-1):
            if lst[idx] >= lst[idx + 1]:
                return False
        return True

    for idx in range(len(sequence) - 1):
        if sequence[idx] >= sequence[idx + 1]:
            fixable = is_increasing([*sequence[:idx], *sequence[idx+1:]]) or is_increasing([*sequence[:idx+1], *sequence[idx+2:]])
            if not fixable:
                return False

    return True"""
