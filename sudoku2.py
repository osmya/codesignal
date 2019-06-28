def sudoku2(a):
    rows = [set(i) for i in a]
    cols = [set(i) for i in list(zip(*reversed(a)))]
    r_iter = iter(rows)
    c_iter = iter(cols)
    return rows, cols
    


grid = [['1', '4', '.'],
        ['.', '6', '.'],
        ['.', '.', '.'],
        ['.', '1', '.']]
        
test = sudoku2(grid)


""" Must have equal len(array) equal to len(i) for i in array
cols = [[x[i] for x in a][::-1] for i in range(len(a))] """ 


# final code minus checking for 3x3 grid..


def sudoku2(a):
    b = list(zip(*reversed(a)))
    rows = [set() for i in a]
    cols = [set() for i in b]
    r_iter = iter(rows)
    c_iter = iter(cols)
    a_iter = iter(a)
    b_iter = iter(b)
    ai = next(a_iter)
    bi = next(b_iter)
    rn = next(r_iter)
    cn = next(c_iter)
    grids = [[x[i] for x in a[0:3] for i in range(3)],
    [x[i] for x in a[3:6] for i in range(3)],
    [x[i] for x in a[6:9] for i in range(3)],
    [x[i] for x in a[0:3] for i in range(3, 6)],
    [x[i] for x in a[3:6] for i in range(3, 6)],
    [x[i] for x in a[6:9] for i in range(3, 6)],
    [x[i] for x in a[0:3] for i in range(6, 9)],
    [x[i] for x in a[3:6] for i in range(6, 9)],
    [x[i] for x in a[6:9] for i in range(6, 9)]]
    sets = [set() for i in grids]
    s_iter = iter(sets)
    gd_iter = iter(grids)
    s1 = next(s_iter)
    gd1 = next(gd_iter)
    result = []
    count = 0
    def row_check(r, y):
        nonlocal count
        k = 0
        while k <= len(y):
            for i in y:
                if i == '.':
                    count += 0
                elif i in r:
                    count += 1
                else:
                    r.add(i)
            k += 1
            r = next(r_iter, None)
            if r is None:
                pass
            y = next(a_iter, None)
            if y is None:
                return count
    def col_check(c, x):
        nonlocal count
        g = 0
        while g <= len(x):
            for i in x:
                if i == '.':
                    count += 0
                elif i in c:
                    count += 1
                else:
                    c.add(i)
            g += 1
            c = next(c_iter, None)
            if c is None:
                pass
            x = next(b_iter, None)
            if x is None:
                return count
    def grid_check(s, gd):
        nonlocal grids
        nonlocal result
        k = 0
        while k <= len(grids):
            for i in gd:
                if i == '.':
                    result += [0]
                elif i in s:
                    result += [1]
                    return result
                else:
                    s.add(i)
            k += 1
            s = next(s_iter, None)
            if s is None:
                pass
            gd = next(gd_iter, None)
            if gd is None:
                return result
    grid_check(s1, gd1)
    row_check(rn, ai)
    col_check(cn, bi)
    if count <= 0 and 1 not in result:
        return True
    else:
        return False

# or return count <=1 and 1 not in result
