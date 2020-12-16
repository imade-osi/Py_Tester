#practice test
# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# def solution(A):
#     smallest_check = 1
#     num_hash = {}
    
#     for ele in A:
#         if ele not in num_hash:
#             num_hash[ele] = True
            
#     while(True):
#         if smallest_check in num_hash:
#             smallest_check += 1
#         else:
#             break
    
#     return smallest_check
    
#     pass



# def solution(N, K):
#     if N == 0:
#         return [""]
#     result = []
#     for p in solution(N - 1, K + 1):
#         for l in "abc":
#             if p[-1:] != l:
#                 result += [p + l]
#     return result[:K]

# print(solution(3,10))


# def solution(A):
#     # write your code in Python 3.6
#     max_val = len(A)
#     num_hash = {}
    
#     for ele in A:
#         if ele not in num_hash:
#             num_hash[ele] = 1
#         else:
#             num_hash[ele] += 1
    
#     while max_val >= 0:
#         if  max_val in num_hash and num_hash[max_val] == max_val:
#             break
#         max_val -= 1
        
#     return max_val

# print(solution([3,4,5,2,8,9,2,3,3]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# def solution(A, B):
   
#     count = 1
#     A1 = sum(A[:1])
#     A2 = sum(A[1:])
#     B1 = sum(B[:1])
#     B2 = sum(B[1:])
    
#     for i in range(1, len(A) - 1):
#         if A1 == A2 and B1 == B2:
#             count += 1
        
#         A1 += A[i]
#         A2 -= A[i]
        
#         B1 += B[i]
#         B2 -= B[i]
        
    
#     return count
#     pass

# def findDuplicates(arr):
# p1, p2
#     return num

# def sortedSquares(nums):
#         return_arr = [0 for ele in range(len(nums))]
#         lp = 0
#         rp = len(nums) - 1
#         return_p = len(nums) - 1
        
#         while lp <= rp:
#             if nums[lp] ** 2 > nums[rp] ** 2:
#                 return_arr[return_p] = nums[lp] ** 2
#                 lp += 1
#             else:
#                 return_arr[return_p] = nums[rp] ** 2
#                 rp -= 1
#             return_p -= 1
               
#         return return_arr

#     input: [-4,-1,0,3,10] 
#     output: [0,1,9,16,100]
        
#    [-4,-1,0,3,10]
#           lr
#            0    
        
#    [0, 1,9,16,100]
#     ^
    


# def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
        
#         for j in range(len(nums)):
#             if nums[i] != nums[j]:
#                 i += 1
#                 nums[i] = nums[j]
            
#         return i + 1
        
        
        
        
#    input: [0,0,1,1,1,2,2,3,3,4]
#    output: 5
    
#             i
#    [0,1,2,3,1,0,2,2,3,4]
#                       j