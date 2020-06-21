# import copy
# Returns true if there is a path from  
# root to the given node. It also  
# populates 'arr' with the given path  
# def hasPath(root, arr, x): 
      
#     # if root is None there is no path  
#     if (not root): 
#         return False
      
#     # push the node's value in 'arr'  
#     arr.append(root.data)      
      
#     # if it is the required node  
#     # return true  
#     if (root.data == x):      
#         return True
      
#     # else check whether the required node  
#     # lies in the left subtree or right  
#     # subtree of the current node  
#     if (hasPath(root.left, arr, x) or 
#         hasPath(root.right, arr, x)):  
#         return True
      
#     # required node does not lie either in  
#     # the left or right subtree of the current  
#     # node. Thus, remove current node's value   
#     # from 'arr'and then return false      
#     arr.pop(-1)  
#     return False
  
# # function to print the path from root to  
# # the given node if the node lies in the binary tree  
# def printPath(root, x): 
      
#     # vector to store the path  
#     arr = []  
      
#     # if required node 'x' is present  
#     # then print the path  
#     if (hasPath(root, arr, x)): 
#         for i in range(len(arr) - 1): 
#             print(arr[i], end = "->")  
#         print(arr[len(arr) - 1]) 
      
#     # 'x' is not present in the  
#     # binary tree  
#     else: 
#         print("No Path")

# def word_flipper(our_string):
#     """
#     Flip the individual words in a sentence

#     Args:
#        our_string(string): String with words to flip
#     Returns:
#        string: String with words flipped
#     """

#     start = -1
#     end = 0
#     new_str = ""
#     our_string += " "

#     for inx, char in enumerate(our_string):
#         if char == " ":
#             end = inx - 1
#             while start < end:
#                 new_str += our_string[end]
#                 end -= 1
#             start = inx
#             new_str += " "
     
#     y = new_str

#     return y


# def max_sum_subarray(arr):
#     max_sum = arr[0]
#     current_sum = arr[0]

#     for num in arr[1:]:
#         current_sum = max(current_sum + num, num)
#         max_sum = max(current_sum, max_sum)
#     return max_sum

# class Stack:
#     def __init__(self):
#         self.items = []

#     def size(self):
#         return len(self.items)

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if self.size() == 0:
#             return None
#         else:
#             return self.items.pop()

# stack = Stack()
# stack.push(0)
# stack.push(1)
# stack.push(2)

# stack.pop()

# print(stack.items)




# q = [3,4,5]
# q.append(1)
# q.append(2)
# q.pop(1)
# print(q)

# word = "happy"
# new_word = word[::-1]
# max_sum_subarray([1, 2, -5, -4, 1, 6])
# print [1] + [3,4,5] 
# print(new_word)


# def is_palindrome(input):
#     """
#     Return True if input is palindrome, False otherwise.
    

#     Args:
#        input(str): input to be checked if it is palindrome
#     """
    
# Todo: Write your recursive palindrome checker here
#     if len(input) == 0:
#         return True
#     elif len(input) == 1:
#         return input
#     else:
#         return ((input[-1] + is_palindrome(input[:-1])) == input)  
  

# print(is_palindrome("madam"))
# print ("Pass" if 'bank' else "Fail")
# def is_list(element):
#     """
#     Check if element is a Python list
#     """
#     return isinstance(element, list)


# def deep_reverse(arr):
#     """
#     Function to deep_reverse an input list
#     """
#     return deep_reverse_func(arr, 0)


# def deep_reverse_func(arr, index):
#     """
#     Recursive function to deep_reverse the input list
#     """
#     # Base Case
#     if index == len(arr):
#         return list()

#     output = deep_reverse_func(arr, index+1)

#     # if element is a list --> deep_reverse the list
#     if is_list(arr[index]):
#         to_append = deep_reverse(arr[index])
#     else:
#         to_append = arr[index]

#     output.append(to_append)
#     return output

# print(14//100)

# l1 = [1,2,3,4,5]
# l2 = copy.deepcopy(l1)
# l2[0] = 5 

# print(l1)
# print(l2)

# def steps(n):
#     if n <= 1:
#         return 1

#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
    
#     return steps(n-1) + steps(n-2) + steps(n-3)

# print(steps(5))

# def b_search(arr, target):
#     if len(arr) == 1:
#         if arr[0] == target:
#             return True
#         else:
#             return False 
    
#     mid = len(arr) // 2

#     if arr[mid] == target:
#         return True
#     elif target < mid:
#         return b_search(arr[:mid], target)
#     elif target > mid:
#         return b_search(arr[mid:], target)


# print(b_search([1,2,3,4,5], 4))    
    
# new_list = [2,3,4,5]
# s = "\n_________________\n".join([str(item) for item in new_list[::-1]])
# print(s)

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2

#     left_half = arr[:mid] 
#     right_half = arr[mid:]

#     left = merge_sort(left_half)
#     right = merge_sort(right_half)

#     return merge(left, right)


# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] > right[right_index]:
#             merged.append(right[right_index])
#             right_index += 1
#         else:
#             merged.append(left[left_index])
#             left_index += 1
        
#     merged += left[left_index:]
#     merged += right[right_index:]
        

#     return merged

# def merge(left, right):

#     merged = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] > right[right_index]:
#             merged.append(right[right_index])
#             right_index += 1
#         else:
#             merged.append(left[left_index])
#             left_index += 1

#     merged += left[left_index:]
#     merged += right[right_index:]

#     return merged

# print(merge_sort([5,3,5,8,5,2,42,25,4,7779]))


# input [3,4,5,5,3,4,1,2,2]
# output [1]

# def single_checker(my_list):
#     my_hash = {}

#     for ele in my_list:
#         if ele in my_hash:
#             my_hash.pop(ele)
#         else:
#             my_hash[ele] = True
#     return my_hash.keys()
        

# print(single_checker([3,4,5,5,3,4,1,2,2]))

# def single_checker(my_list):
#     my_list.sort()
    
#     ptr1 = 0
#     ptr2 = 1

#     while ptr2 < len(my_list):
#         if my_list[ptr1] ^ my_list[ptr2]:
#             return my_list[ptr1]
#         ptr1 += 1
#         ptr2 += 1

# print(single_checker([3,4,5,5,3,4,1,2,2]))

# def b_search(arr, target):
#     if len(arr) == 1:
#         if arr[0] == target:
#             return True
#         else:
#             return False

#     mid = len(arr) // 2

#     if arr[mid] == target:
#         return True 
#     elif target < arr[mid]:
#         b_search(arr[:mid], target) 
#     elif target > arr[mid]:
#         b_search(arr[mid:], target) 


# print(b_search([1,2,3,5,8,9], 0))

# def quick_sort(my_list):
#     if len(my_list) <= 1:
#         return my_list

#     pivot_index = quick_work(my_list)

#     left = my_list[:pivot_index]
#     right = my_list[pivot_index:]

#     quick_sort(left)
#     quick_sort(right)

#     return my_list

# def quick_work(items):
    # pntr1 = 0
    # pntr2 = len(my_list) - 1

    # while pntr1 < pntr2:
    #     if my_list[pntr1] < my_list[pivot]:
    #         pntr1 += 1
    #     elif my_list[pntr1] > my_list[pivot]:
    #         if my_list[pntr2] < my_list[pivot]:
    #             my_list[pntr1], my_list[pntr2] = my_list[pntr2], my_list[pntr1]
    #         else:
    #             pntr2 -= 1
            
    # return def deletion_distance(str1, str2):
    # count = 0

    # if len(str1) > len(str2):
    #     for inx, char in enumerate(str1):
    #         if str1_arr[inx] not in str2:
    #             count += 1
#     else:
#         for inx, char in enumerate(str2):
#             if str2_arr[inx] not in str1:
#                 count+=1

    # return count


#     pivot_index = len(items) - 1
#     left_index = 0
#     pivot_value = items[pivot_index]

#     while (pivot_index != left_index):

#         item = items[left_index]

#         if item <= pivot_value:
#             left_index += 1
#             continue

#         # Place the item before the pivot at left_index
#         items[left_index] = items[pivot_index - 1]
#         # Shift pivot one to the left
#         items[pivot_index - 1] = pivot_value
#         # Place item at pivot's previous location
#         items[pivot_index] = item
#         # Update pivot_index
#         pivot_index -= 1

#     return pivot_index

# print(quick_sort([5,4,9,15,0,4,2,9]))

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         if not nums: return []
#         nums.sort()
#         L, dic, Set, M = len(nums), {j:i for i, j in enumerate(nums)}, set(), nums[-1]
#         for i in range(L-3):
#             a = nums[i]
            # if a + 3*M < target: continue
            # if 4*a > target: break
            # for j in range(i+1, L-2):
            #     b = nums[j]
            #     if a + b +2*M < target: continue
            #     if a + 3*b > target: break
            #     for k in range(j+1, L-1):
            #         c = nums[k]
        #             d = target-(a+b+c)
        #             if d > M: continue
        #             if d < c: break
        #             if d in dic and dic[d] > k:
        #                 Set.add((a,b,c,d))
        # return Set

#         def find_duplicates(arr1, arr2):
#   #arr1_hash = {}
#   solutions_arr = []
#   arr1_pnt = 0
#   arr2_pnt = 0
  
#   while arr1_pnt < len(arr1) and arr2_pnt < len(arr2):
#     if arr1[arr1_pnt] < arr2[arr2_pnt]:
#         arr1_pnt += 1
#     elif arr2[arr2_pnt] < arr1[arr1_pnt]:
#         arr2_pnt += 1
#     else:
#         solutions_arr.append(arr1[arr1_pnt])
#         arr1_pnt += 1
#         arr2_pnt += 1
        
#   return solutions_arr

# Island Count
# This problem is very similar to counting the number of connected components in an Undirected Graph. However, Graph Theory isn’t necessary to solve this problem or to understand its solution. In an undirected graph, a connected component is a group of vertices in which every vertex is connected to at least one other vertex. In a similar way, an island in the matrix is a group of adjacent (connected) 1s.

# To solve this problem, we’ll traverse binaryMatrix and every time we come across a cell of 1 we’ll do the following: Change that cell and all its vertically and horizontally (but not diagonally) adjacent 1s into -1s. We do this “expansion” in order to avoid recounting of islands. Increment islands - which is our counter for number of islands - by 1. Expanding from a cell whose value is 1 to other adjacent 1s in binaryMatrix is similar to running a Breadth-First Search (BFS) or a Depth-First Search (DFS).

# In our case, we’ll avoid using a recursion and instead opt for an iterative approach to expand to all adjacent 1s. We do so by using queue that holds the next indices to visit. We keep expanding to other adjacent 1s as long as the queue is not empty. Whenever we encounter a value of -1 in our traversal, we ignore it since it is part on an island we’ve already counted.

# Pseudocode:

# function getNumberOfIslands(binaryMatrix):
#     islands = 0
#     rows = binaryMatrix.length # number of rows
#     cols = binaryMatrix[0].length # number of columns

#     for i from 0 to rows-1:
#         for j from 0 to cols-1:
#             if (binaryMatrix[i][j] == 1):
#                 markIsland(binaryMatrix, rows, cols, i, j)
#                 islands++
                
#     return islands


# function markIsland(binaryMatrix, rows, cols, i, j):
#     q = new Queue()
#     q.push([i,j])
#     while (!q.isEmpty()):
#         item = q.pop()
#         x = item[0]
#         y = item[1]
#         if (binaryMatrix[x][y] == 1):
#             binaryMatrix[x][y] = -1
#             pushIfValid(q, rows, cols, x-1, y)
#             pushIfValid(q, rows, cols, x, y-1)
#             pushIfValid(q, rows, cols, x+1, y)
#             pushIfValid(q, rows, cols, x, y+1)


# function pushIfValid(q, rows, cols, x, y):
#     if (x >= 0 AND x < rows AND y >= 0 AND y < cols):
#         q.push([x,y])

# Time Complexity: let N and M be the numbers of columns and rows in binaryMatrix, respectively. Each cell in binaryMatrix is visited a constant number of times. Once during the iteration and up to 4 times during an island expansion. Therefore, the time complexity is linear in the size of the input, i.e. O(N⋅M).

# Space Complexity: since we are allocating a queue in the algorithm, the space complexity is linear O(N⋅M). For instance, consider a matrix that is all 1s.

# Array Quadruplet
# The naive solution would be to consider every quadruplet in the input array and return the one (if exists) whose sum is s. This approach requires using 4 nested loops and its time complexity is O(N^4). This is quite inefficient and we can do better than that.

# We start by sorting the given array in ascending order and then for each pair (arr[i], arr[j]) in the array where (i < j), we check if a quadruplet is formed by current pair and a pair from a subarray arr[j+1...n-1]. So how do we find a complementing pair in the subarray arr[j+1...n-1]?

# What we want to do is to find two values in the subarray such that their sum equals to s - (arr[i], arr[j]). Let’s denote this value as r. Now, since we made sure to sort arr in an ascending order, the idea is to maintain the search space by keeping two indexes (low and high) that initially point to two end-points of the subarray. Then we loop until low is less than high and reduce the search space arr[low...high] at each iteration of the loop. We compare the sum of the values present at index low and high with r and increment low if the sum is less than r and decrement high if the sum is more than r. Finally, if the sum is equal to r, we found the desired pair.

# The quadruplet will then consist of the initial pair we found in the first step and the complementing pair we found in the subarray.

# Pseudocode:

# function findArrayQuadruplet(arr, s):
#     n = arr.length

#     # if there are fewer than 4 items in arr, by
#     # definition no quadruplet exists whose sum is s
#     if (n < 4):
#         return []

#     # sort arr in an ascending order
#     arr.sort()

#     for i from 0 to n - 4:
#         for j from i + 1 to n - 3:
#             # r stores the complementing sum
#             r = s - (arr[i] + arr[j])

#             # check for sum r in subarray arr[j+1…n-1]
#             low = j + 1, high = n - 1;

#             while (low < high):
#                 if (arr[low] + arr[high] < r):
#                     low++

#                 else if (arr[low] + arr[high] > r):
#                     high--

#                 # quadruplet with given sum found
#                 else:
#                     return [arr[i], arr[j], arr[low], arr[high]]

#     return []
# Time Complexity: we have three nested loops whose combined time complexity is O(N^3), where N is the size of arr. We also using sorting in the beginning and that’s additional O(N⋅log(N)). The total time complexity is still O(N^3) because O(N⋅log(N)) gets thrown away since in the asymptotic calculation it’s not material.

# Space Complexity: O(1) as we used only a constant amount of space throughout the algorithm.

# Root of Number
# The solution presented here is much like a binary search in a sorted array.

# Pseudocode:

# function root(x, n):
#     if (x == 0):
#         return 0

#     lowerBound = 0
#     upperBound = max(1, x)
#     approxRoot = (upperBound + lowerBound) / 2

#     while (approxRoot - lowerBound >= 0.001):
#         if (power(approxRoot, n) > x):
#             upperBound = approxRoot
#         else if (power(approxRoot, n) < x):
#             lowerBound = approxRoot
#         else
#             break

#         approxRoot = (upperBound + lowerBound) / 2

#     return approxRoot
# As we can see, the function finds an initial lower and upper bound for the answer, and sets the initial guess for the answer to be the average. Then the iteration begins, and the we notice that the following facts are true in every step of the iteration:

# (approxRoot - lowerBound) = ½(upperBound - lowerBound) - Since approxRoot is always the average value between upperBound and lowerBound.
# At the end of every iteration, the real root always satisfies the inequality lowerBound < root < upperBound: this is true since in the beginning of the iteration, we check if approxRoot to the power of n is greater than or lesser than x. The power function is monotonically increasing (i.e. a < b dictates that a^n < b^n) meaning this indicates whether the approximation is too high or too low.
# The value of (upperBound - lowerBound) is cut by half in every iteration - since in every step we replace one of the values of upperBound or lowerBound by their current average. Obviously it means that eventually the distance between the bounds is lower than 0.001. Since the real root is between the bounds, this promises the algorithm stops.
# Thus, since lowerBound< root < upperBound, then the true error - |root-approxRoot|, satisfies |root-approxRoot| < (approxRoot - lowerBound) - so it is indeed enough to check when the value on the right side is lower than 0.001.
# Thus the algorithm always stops, and output of the algorithm is correct.

# The best way to explain the solution algorithm is by using it on an example. Let’s try calculating the 3rd root of 7: We mark the real root as y ≅ 1.912931182772389. Our method shall iterate in a main loop, and try to produce a sequence of approximations that converge to y, until reaching a number that is close enough.

# Iteration 1: Initially, we recognized that 0 < y, since 03 = 0 < 7. Also y < 7. Thus lowerBound = 0 and upperBound = 7. Our first member of the sequence is chosen to be the average between 0 and 7 - approxRoot = 3.5. Since 3.53 ≅ 42.8 > y, then we conclude that 0 < y < 3.5, so we conclude upperBound = 3.5. Note that the error is bounded: |y - approxRoot| < |3.5 - 0| = 3.5.

# Iteration 2: Since we concluded that 0 < y < 3.5, our second member of the sequence should be, again, the average between our bounds 0 and 3.5 - approxRoot= 1.75. This time 1.753 ≅ 5.3 < 7, which means 1.75 < y < 3.5, so we update lowerBound = 1.75. The error is bounded by: |y - approxRoot| < |upperBound - lowerBound|= |3.5- 1.75| = 1.75. We continue the sequence this way, and notice that the error bound is reduced by half by every iteration. Here is a summary of the first few iterations in this method:

# # Iteration	LowerBound	UpperBound	approxRoot value	|y- approxRoot| - True Error	Error bound
# 1	0	7	3.5	≅ 1.58	< 3.5 (7×2-1)
# 2	0	3.5	1.75	≅0.16	< 1.75 (7×2-2)
# 3	1.75	3.5	2.625	≅0.71	< 0.875 (7×2-3)
# 4	1.75	2.625	2.1875	≅0.27	< 0.4375 (7×2-4)
# As we can see, by choosing the average value between By the 13th iteration, we’ll reach an error bound of 7×2^(-13), which is less than 0.001 (notice that the error may be much smaller, but since we don’t actually know the real value of y in the process of computation, we cannot promise a better bound).

# Time Complexity: notice that every loop iteration is done in O(1), under the assumption that the power function takes a constant time. The initial error is x, and the error is multiplied by 0.5 in every iteration. Thus the number of iterations is the minimal k such that: 2^(-k) x<0.001 i.e. 2^(-k)<(0.001 / x) k >log(x) + 3log(10) = O(log(x)) The number of iterations is therefore O(log(x)), meaning the total runtime is O(log(x)) if we refer to the value stored in x, or O(x) if we refer to the number of bits required to represent x (since it takes Log(x) in average bits to represent a number x).

# Space Complexity: O(1), since we only need a constant number of variables for the algorithm.

# Mathematical Note: our explanation used the fact that power function x^n is a monotonically increasing continuous function on the positive numbers. Although it is true, the Intermediate value theorem in calculus, states that this method will work for every continuous function - but the proof for this requires more mathematical tools.
'''
brute force
  sort on the whole array
  quick sort
  runtime O(n log n)
  space O(1)
  
solution1 
  [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
      i 
                  j
  k=2
  sliding window 2k + 1 
  runtime n k log k
  
solution 2
  use heap 
  time: n log k
  space: n

create a heap with first 2k + 1 elements
iterate from 2k + 1 end of array
  pop from heap
  put cur element onto heap
  
if we are at the end of array
  keep poping from heap until empty

'''

# from queue import PriorityQueue
# https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3
  
# import heapq

def sort_k_messed_array(arr, k):
  q = []
  
  result = []
  for num in arr:
    heapq.heappush(q, num)
    if len(q) > 2 * k + 1:
      result.append(heapq.heappop(q))
  while q:
    result.append(heapq.heappop(q))
  return result  
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
# heap_size = 5
# heap = []
#result = [1 2 3 4 5 6 7 8 9 10]
# print(sort_k_messed_array(arr, k))
# print(sort_k_messed_array(arr, k))


