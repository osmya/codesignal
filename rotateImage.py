#############
####LIKE#####
#############

# list comprehension like the most
def rotateImage(a): # did similar in data notebook
    return [[x[i] for x in a][::-1] for i in range(len(a))] 

# my origianl sol

def rotateImage(a): # i did not know how zip works
    start = min(range(len(a)))
    end = max(range(len(a)))
    unitmin = min(range(len(a[0])))
    rotated = []
    def makearr(arr_maxidx, arr, index):
        new_arr = []
        for i in arr:
            while index >= 0:
                number = arr[index][arr_maxidx]
                new_arr.append(number)
                index -= 1
        return new_arr
    while start <= end:
        rotated.append(makearr(unitmin, a, end))
        start += 1
        unitmin += 1
    return rotated


# alternative solution (create tuples?) *** should use list in front

a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rotateImage = lambda a: zip(*a[::-1]) # reverses a then zip
sol = rotateImage(a)
>>> sol
[(13, 9, 5, 1), (14, 10, 6, 2), (15, 11, 7, 3), (16, 12, 8, 4)]


# alternative solution using reverse method

def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

# alternative solution with zip

def rotateImage(a):
    return list(zip(*reversed(a)))
# check this for *func https://stackoverflow.com/questions/13635032/what-is-the-inverse-function-of-zip-in-python

""" When used like this, the * (asterisk, also know in some circles as the "splat" operator) is a signal to unpack 
arguments from a list. See http://docs.python.org/tutorial/controlflow.html#unpacking-argument-lists
for a more complete definition with examples.

https://stackoverflow.com/questions/5917522/unzipping-and-the-operator
"""

