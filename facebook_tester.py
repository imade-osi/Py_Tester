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
# String s1
# String s2
# String s1 + s2

# input: "18","13"
#               ^
# output: "23"    
#     [0,1,2,3,4,5,6,7,8,9]   
#     1
#     18
#     ^
# +   13
#     ^
#     31
#      ^ 
    
# def add_remainder(sum):
#     nem_sum = ""
    
#     new_sum.prepend(sum[1])
    
#     return new_sum
       
# def sum_calc(str1, str2):
#     sum1 = ""
#     sum2 = ""
    
#     num_hash ={"0": 0, "1": 1,  1,2,3,4,5,6,7,8,9} 
#     for digit in range(-1, len(str1)):
        
#         if sum > 9:
#             add_remainder(sum1) 
#         else: 
#         sum1.prepend(num_hash[str1[digit]] + num_hash[str2[digit]])
           
# #     for digit in range(-1, len(str2)):
        
# #         sum1.prepend(num_hash[str1[digit]] + num_hash[str2[digit]])
      
#     return sum










# Part 2.) Understanding Arrays

#Today's Lesson: Arrays!

# my_array = [8,6,7,5,3,0,9]

# print(f"Array value at index 1: {my_array[1]}")
# print(f"Array value at index 2: {my_array[2]}")
# print(f"Array[1] + Array[2]: {my_array[1] + my_array[2]}")


#    **** Class Activity!!! *****
#   Onlineclicker.org => Poll Number 1002 

#      1.) 14

#      2.) 13

#      3.) 12

#      4.) Error with question




# Part 3.)  Example Problem 

Q.) Given an array of both positive and negative integers. 
The task is to sort the square of the numbers of the Array. 

Examples: 
Input  : arr = [5, 3, -1, 2, -4]
Output : [1, 4, 9, 16, 25] 



#    **** Class Activity!!! *****
#   Onlineclicker.org => Poll Number 1003

# 1.) [25, 9, 1, 4, 16] 

# 2.) [-4, -1, 2, 3, 5]

# 3.) [1, 4, 9, 16, 25] 

# 4.) Not enough info to solve

 



#arr =  [5, 3, -1, 2, -4]
#                ^




      
# 1.) Loop through Indices: 

#  0  1   2   3   4
# [5, 3, -1,  2, -4]
#  ^


# 2.) Square values:
#    [25, 9, 1, 4, 16] 
             


# 3.) Sort Values: 
#    [1, 4, 9, 16, 25] 



# 4.) return sorted array 


def sorted_arr(arr):

    #1.)
    for i in range(len(arr)):   
        #2.)
        arr[i] = arr[i] * arr[i]  
        
    #3.)
    arr.sort() 
    
    #4.)
    return arr



# print(f"Before sort: {[5, 3, -1, 2, -4]} ")

# print(f"After sort: {sorted_arr([5, 3, -1, 2, -4])}")







#STAY TUNED NEXT WEEK FOR HASHES!!! {}

["19-0001", HDD, RAM, GPU, HDD, GPU, Chassis, GPU]
                 
 [ GPU, HDD, GPU, RAM] 

'RAM' = 1
'GPU' = 2
'HDD' = 1


    pallet_size += 1
    'GPU' = 1
    'HDD' = 2
       
    window[8] = arr[8]

pallet_size = 5

pallets_with_repetitions = 3

n*k

def partition_count(arr, size):
    window = [ for ele in range(size)] 
    part_hash = {}
    pallet_rep = 1
    front = 0
    end = size - 1
    
    for i in range(len(size)):
        window[i] = arr[i]
        
        # if key not in part_hash:
        # del part_hash key

        
        
        if i == size:
            for ele in window:
                if ele in part_hash:
                   pallet_rep += 1
                else:
                    part_hash[ele] = True
            part_hash = {}
    
    return pallet