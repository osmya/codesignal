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
