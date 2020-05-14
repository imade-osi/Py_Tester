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
# # the given node if the node lies in 
# # the binary tree  
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
    
#     # TODO: Write your recursive palindrome checker here
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
            if a + 3*M < target: continue
            if 4*a > target: break
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b +2*M < target: continue
                if a + 3*b > target: break
                for k in range(j+1, L-1):
                    c = nums[k]
                    d = target-(a+b+c)
                    if d > M: continue
                    if d < c: break
                    if d in dic and dic[d] > k:
                        Set.add((a,b,c,d))
        return Set