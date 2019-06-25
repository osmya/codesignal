def rotateImage(a):
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
