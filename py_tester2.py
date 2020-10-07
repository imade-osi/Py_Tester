# def spiral_copy(inputMatrix):
#   pass # your code goes here

#naive solution
#iterate through 2d array 
#collect ints in order to return array
#iterate to next spiral cordinate
#collect element until end of spiral into return array
#the return the return array


# ~~~~~~~spiral logic~~~~~~~~~~~

# i = 0

# ~~~~~~~~~~~~going right ==> ~~~~~~~~~
# start at first row (2d_array[i])
# iterate through first row 
# going right ==>   #also have visited logic to make sure i dont renter cord (cl)
# len(2d_array[0]) - 1 until 0
# (2d_array)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
#                          [16,  17,  18,  19,  21] ]

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


# print(array_of_array_products([3]) 
# print(array_of_array_products([2]) 
# print(array_of_array_products([1]) 


def fib_helper(n, memo):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  if n not in memo:
    memo[n] = fib_helper(n-1, memo) + fib_helper(n-2, memo)

  return memo[n]

def memo_fib(n):
  memo = {}
  return fib_helper(n, memo)

print(memo_fib(5))





# def fib(n):

#     fib_arr = []

#     if n <= 0:
#         return 0
#     elif n < 2: 
#         return 1

#     return fib(n-1) + fib(n-2)

# def iterative_fib(num):

#     fib[0] = 0
#     fib[1] = 1

#     # for i in range(2, num):
#     #     fib[i] = fib[i-1] + fib[i-2]

#     return fib[num]

#     print(iterative ib(0))


# def minOp(str1, str2):
#     str_count = 0

#     if len(str1) < len(str2):
#         for ele in str1:
#             if ele in str2:
#                 str_count +=1 
#     else:
#         for ele in str2:
#             if ele in str1:
#                 str_count +=1 

#     return max(len(str1), len(str2)) - str_count

# print(minOp('sundayy', 'sunday'))



#   def minOp(str1, n, str2, m):

#             if (m == 0):
#                 return n

#             if (n == 0):
#                 return m

#             if (str1[n-1] == str2[m-1]):
#                 return minOp(str1, n -1, str2, m -1)

#             return 1 + (min(minOp(str1, n, str2, m-1),  minOp(str1, n-1, str2, m), minOp(str1, n-1, str2, m-1)))

#         return minOp(word1, len(word1), word2, len(word2))



# def second_largest(arr):
#     max_num = 0
#     max_inx = None
#     sec_max = 0

#     for inx, ele in enumerate(arr):
#         if ele > max_num:
#             max_num = ele
#             max_inx = inx

#     for inx, ele in enumerate(arr):
#         if ele > sec_max and ele <= max_num and inx!= max_inx:
#             sec_max = ele
    
#     return sec_max

# print(second_largest([2,3,4,4 ]))


# Problem Statement #
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
#
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
#
# Example 1:
#
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:
#
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and

# def num_decodings(str)
#   result = []
#   cur = []
#   _num_decodings(cur, str, result)
#   result.count
# end

# def _num_decodings(cur, rem, result)
#   if rem.nil? || rem.empty?
#     result << cur
#     return
#   end

#   unless rem[0] == "0" || rem[1] == "0"
#     cur_1 = cur.clone
#     cur_1  << rem[0]
#     _num_decodings(cur_1, rem[1..-1], result)
#   end

#   if rem[0..1].to_i.between?(10,26)
#     cur_2 = cur.clone
#     cur_2 << rem[0..1]
#     _num_decodings(cur_2, rem[2..-1], result)
#   end
# end


# def num_decodings_dp(s)
#   if s.nil? || s.empty? || s[0] == '0'
#     return 0
#   end

#   dp = Array.new(s.length + 1, 0)
#   dp[0] = 1
#   dp[1] = 1
#   i = 2

#   while i <= s.length
#     dp[i] += dp[i-1] if s[i-1] > '0'
#     dp[i] += dp[i-2] if s[i-2..i-1].between?('10', '26')
#     i += 1
#   end

#   dp[i - 1]
# end    
#                            inx 0
#                           0 1 2 3
#   #                      "1 1 1 2"
#                   //                 \\
#                 A inx 1[112]         K inx2[12]
#               //     \\             //      \\ 
#             AA [12]   AK[2]       KA[2]      KL 
#             //  \\    //   \\     //   \\ 
#          AAA[2]  KL  AKB     0   KAB     0
#          //  \\ 
#       AAAB    0

# "1112"  
#    ^      

# def decode_ways(str, inx):
#   if inx == len(str)
#     return 1

#   if str[inx] == '0':
#     return 0

#   way1 = decode_ways(str, inx+1)
#   if int(str[inx:inx+2]) <= 26 and inx+2 <= len(str):
#     way2 = decode_ways(str, inx+2)
#   else:
#     way2 = 0

#   return way1 + way2

#print(decode_ways(""))

 
cache = {}
def decode_ways(code, inx):
  if inx == len(code):
    return 1

  way1 = way2 = 0
  if inx not in cache:
    if 1<= int(code[inx]) <=9:
      way1 = decode_ways(code, inx+1)
    if 10<= int(code[inx:inx+2]) <= 26:
      way2 = decode_ways(code, inx+2)
    cache[inx] = way1 + way2

  return cache[inx]

print(decode_ways("1112", 0))


# for i in range(1, 2000):
#   print(i, ":", decode_ways(str(i), 0))

# str = "11"
# print(str[1:10])

# cache = {}
# def numDecodings(s, index=0):
#         if(index==len(s)):
#             return 1
#         if(index in cache):
#             return cache[index]
#         ret = 0
#         if(1<=int(s[index])<=9):
#             ret += numDecodings(s,index+1)
#         if(10<=int(s[index:(index+2)])<=26):
#             ret += numDecodings(s,index+2)
#         cache[index]=ret
#         return ret

# print(numDecodings('01', 0))


# def closest_leaf(root, k):
#   if len(root) == 1 and k == root[0]
#   return k

# def runningSum(nums):

#   for i in range(1, len(nums)):
#     nums[i] = nums[i - 1] + nums[i]
  
#   return nums 

# print(runningSum([3,1,2,10,1]))

# def dfs(node, l, r):
#   if l <= node.val <= r
#     ans += node.val
#   if l < node.val:
#     dfs(node.left)
#   if r > node.val:
#     dfs(node.right)

# def rangeSumBST(root, l, r):
#   ans = 0
#   dfs(root, l, r)
#   return ans

# print(isinstance(100.0, int))



  

