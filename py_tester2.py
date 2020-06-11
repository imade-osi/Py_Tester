# def spiral_copy(inputMatrix):
#   pass # your code goes here



#naive solution
#iterate through 2d array 
#collect ints in order to return array
#iterate to next spiral cordinate
#collect element until end of spiral into return array
#return that return array


# ~~~~~~~spiral logic~~~~~~~~~~~~~

# i = 0

# ~~~~~~~~~~~~going right ==> ~~~~~~~~~
# start at first row (2d_array[i])

# iterate through first row 
# going right ==>   #also have visited logic to make sure i dont renter cord (cl)
# len(2d_array[0]) - 1 until 0
# (2d_array)

# ~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~going down ~~~~~~~~~~~~~~

#start iteration at one row below 
#2d_array[i+1]
#iterate down column n-1 until i reach row n or length of the 2d array 
#collect those elements into my return array
#also have visited logic of column n-1 so i dont renter  
#(cl)

#len(2d_array) - 1 until 0

#going left 
#start iteration at column to left  
#2d_array[][]


#going up


# def s_flatten(arr):
 
#   return_arr = []
  
  
#   while len(return_arr) < len(arr):
    
#     for inx, row in enumerate(arr): #right
      
#     for inx, col in enumerate(row):

#     for inx, col in enumerate(row):

#     for inx, col in enumerate(row):
#       return_arr.append(col)
      
      
#     return return_arr
        



# def is_within_bounds(nrows, ncols, row, col):
#    return row >= 0 and row < nrows and col >= 0 and col < ncols

# def find_next_pos(direction, row, col):
#   if direction == 0:
#     col += 1
#   elif direction == 1:
#     row += 1
#   elif direction == 2:
#     col -= 1
#   elif direction == 3:
#     row -= 1
#   return (row, col)

# def find_next_valid_pos(grid, nrows, ncols, visited, direction, row, col):
#   next_row, next_col = find_next_pos(direction, row, col)
#   if not is_within_bounds(nrows, ncols, next_row, next_col) or (next_row, next_col) in visited:
#     direction = (direction + 1) % 4
#     next_row, next_col = find_next_pos(direction, row, col)    
#   return (direction, next_row, next_col)

# def spiral_copy(inputMatrix):
#   nrows = len(inputMatrix)
#   ncols = len(inputMatrix[0])
#   direction = 0
#   row = 0
#   col = 0
#   visited = set()
#   result = []
#   while (len(result) < nrows * ncols):
#     result.append(inputMatrix[row][col])
#     visited.add((row, col))
#     direction, row, col = find_next_valid_pos(inputMatrix, nrows, ncols, visited, direction, row, col)
#   return result
  
# inputMatrix  = [ [1,    2,   3,  4,    5],
#                          [6,    7,   8,  9,   10],
#                          [11,  12,  13,  14,  15],
#                          [16,  17,  18,  19,  20] ]

# print(spiral_copy(inputMatrix))







#naive solution
#create helper method flip

#outer method
#iterate through the array checking for greatest number 
#once found call flip with index of greatest number 
#call flip with decreasing boundary 

#flip method
#flip number from begining to index of greatest number or k


#main function
#1 iterate
#if i+1 is less then i call flip with i as k


#flip function 
#1




# def flip(arr, k):
  
#   new_arr = []
#   inx = k 
  
#   while inx >= 0:
#     new_arr.append(arr[inx])
#     inx -= 1 
    
#   arr[:k+1] = new_arr
    
  

# def pancake_sort(arr):
  
#   inx = len(arr) - 1 
  
  
#   while inx >= 0:
#     max_num = 0
#     max_inx = 0
    
#     for inx, ele in enumerate(arr[:inx + 1]):
#       if ele > max_num: # mark
#           max_num = ele
#           max_inx = inx
          
#     flip(arr, max_inx)
#     flip(arr, inx)
    
#     inx -= 1
    
#   return arr
    
#     '''
# 8  10  2
# 20       16       80
# 10 x 2   8 x 2   8 x 10

# left_products = 1
# right_products = 1
# [2, 7 ,3, 4]


# [1, 1, 1, 1]
# left_products = 
# 1 [1, 1, 1, 1]
#    ^

# 2 [1, 2, 1 ,1]
#       ^
# 14 [1, 2, 14, 1]
#           ^
# 42 [1, 2, 14, 42]
#                ^
# right_products
# 1  [1, 2, 14, 42]
#                ^
# 4  [1, 2, 14, 42]
#            ^
# 12   [1, 2, 56, 42]
#          ^
# 84     [84, 24, 56, 42]
# '''

# def array_of_array_products(arr):
#   if len(arr) <= 1:
#     return []
#   left_prod = right_prod = 1
#   res = [1 for _ in range(len(arr))]
#   #[1,1,1]
#   # iterate from left to right
#   for i in range(len(arr)):
#     res[i] *= left_prod
#     # [1, 8, 80]
#     left_prod *= arr[i]
#     # 160
#   # from right to left
#   for j in range(len(arr) - 1, -1, -1):
#     res[j] *= right_prod
#     # [20, 16, 80]
#     right_prod *= arr[j]
#     # 160
#   return res

print(array_of_array_products([1]) 
print(array_of_array_products([3]) 
print(array_of_array_products([2]) 

    

  

