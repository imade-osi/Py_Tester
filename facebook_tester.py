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

# grid:
# [[".",".","4",".",".",".","6","3","."], 
#  [".",".",".",".",".",".",".",".","."], 
#  ["5",".",".",".",".",".",".","9","."], 
#  [".",".",".","5","6",".",".",".","."], 
#  ["4",".","3",".",".",".",".",".","1"], 
#  [".",".",".","7",".",".",".",".","."], 
#  [".",".",".","5",".",".",".",".","."], 
#  [".",".",".",".",".",".",".",".","."], 
#  [".",".",".",".",".",".",".",".","."]]

# def sudoku2(grid): 
#     row_count = {}
#     col_count = {}
    
#     for i in range(len(grid)):
#         col_count[i] = {}
        
#         for j in range(len(grid[0])):
#             if grid[i][j] != ".":
#                 if grid[i][j] not in col_count[i]:
#                      col_count[i][grid[i][j]] = True
#                 if grid[i][j] not in row_count:
#                     row_count[grid[i][j]] = True
#                 else:
#                     return False
#         row_count = {}
         
#     return True 




# Welcome to Facebook!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!

# input sorted: [-6, -5, 2, 3, 4]
# squared value:[36, 25, 4, 9, 16]
# output sorted:[36, 25, 16, 9, 4] or [4, 9, 16, 25, 36]

input : [-6, -5, 2, 3, 4]
output: [36, 25, 4, 9, 16] => sorted (my pref)
    
# 1.) [-6, -5, 2, 3, 4]
#       ^
# 2.) [36, 25, 4, 9, 16]

# 3.) sort 

# 4.) return sorted array 


def sorted_arr(arr):
    sorted_return = []
    
    if len(arr) == 0:
        return []
    
    
    for ele in arr:
        ele = ele*ele
        sorted_return.append(ele)
    
    sorted_return.sort()
    
    return sorted_return


    
String s1
String s2
String s1 + s2

input: "18","13"
              ^
output: "23"

    
    [0,1,2,3,4,5,6,7,8,9]
    
    
    
    1
    18
    ^
+   13
    ^
    31
     ^ 
    
def add_remainder(sum):
    nem_sum = ""
    
    new_sum.prepend(sum[1])
    
    return new_sum
    
    
def sum_calc(str1, str2):
    sum1 = ""
    sum2 = ""
    
    num_hash ={"0": 0, "1": 1,  1,2,3,4,5,6,7,8,9}
    
    for digit in range(-1, len(str1)):
        
        if sum > 9:
            add_remainder(sum1) 
        else: 
        sum1.prepend(num_hash[str1[digit]] + num_hash[str2[digit]])
        
    
#     for digit in range(-1, len(str2)):
        
#         sum1.prepend(num_hash[str1[digit]] + num_hash[str2[digit]])
        
    
    return sum

    