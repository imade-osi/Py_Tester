# a = [float(x) for x in range(10, 21) if x %2 == 0]
# print(f'array a:{a}')


# b = [[x for x in range(4)] for j in range(4) ]
# print(f'array b: {b}')

# a = [[1,2,3], 
#     [4,5,6], 
#     [7,8,9]]

# a.reverse()
# print(f'array: {a}')

# x = 10 
# y = 5

# x, y = y, x

# print('x =', x, 'thank you')
# print(f'y = {y}')

# def rotateImage(a):
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(i):
#             a[i][j], a[j][i] = a[j][i], a[i][j]
#     return a

grid:
[[".",".","4",".",".",".","6","3","."], 
 [".",".",".",".",".",".",".",".","."], 
 ["5",".",".",".",".",".",".","9","."], 
 [".",".",".","5","6",".",".",".","."], 
 ["4",".","3",".",".",".",".",".","1"], 
 [".",".",".","7",".",".",".",".","."], 
 [".",".",".","5",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."]]

def sudoku2(grid): 
    row_count = {}
    col_count = {}
    
    for i in range(len(grid)):
        col_count[i] = {}
        
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                if grid[i][j] not in col_count[i]:
                     col_count[i][grid[i][j]] = True
                if grid[i][j] not in row_count:
                    row_count[grid[i][j]] = True
                else:
                    return False
        row_count = {}
         
    return True 

input : [-6, -5, 2, 3, 4]
output: [36, 25, 4, 9, 16] => sorted (my pref)
    
1.) [-6, -5, 2, 3, 4]
      ^
2.) [36, 25, 4, 9, 16]

3.) sort 

4.) return sorted array 


def sorted_arr(arr):
    sorted_return = []
    
    if len(arr) == 0:
        return []
    
    
    for ele in arr:
        ele = ele*ele
        sorted_return.append(ele)
    
    sorted_return.sort()
    
    return sorted_return

