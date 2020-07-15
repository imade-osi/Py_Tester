# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     #def reverseList(self, head: ListNode) -> ListNode:

#        # # 1 -> 2 -> 3 -> 4 -> 5
#        #   ^
#        # # 1 <- 2 <- 3 <- 4 <- 5

#         prev = None
#         curr = head

#         while curr is not None:
#             temp_next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp_next

#         return prev


#given [2,3,-1,2,4,8], target = 0
#         ^
#output  [[1,2,3], [2,3,4], [3,2,1]]


#novice solution

#start at first index of arr
#iterate through array for values after first index
# perform two sum operations on sub array
# collect triplet into return array if found
# move onto next index in outer loop


# def find_unique_triplets(arr, target):

#     trip_hash = {}

#     for outer_ele in arr:

#         for inner in

#     return []

def recurse_prac(n):

    if (n < 0):
        return
    print(" " + str(n))

    #The last executed statement is recursive call
    #recurse_prac(n-1)


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)


def linear_fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
   
    cache = [0,1]

    for inx in range(2, n+1):
        cache.append(cache[inx-1] + cache[inx-2])


    return cache[n]

# print(linear_fib(3))


def pivotIndex(nums):
    if len(nums) < 3:
        return -1

    left_sum = sum(nums[:1])
    right_sum = sum(nums[2:])

    for inx in range(1, len(nums) - 1):
        if left_sum == right_sum:
            return inx

        left_sum += nums[inx]
        right_sum -= nums[inx + 1]

    return -1


# print(pivotIndex([1, 7, 3, 6, 5, 6]))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:

# 	def __init__(self, head: ListNode):
# 	"""
# 		@param head The linked list's head.
# 		Note that the head is guaranteed to be not null, so it contains at least one node.
# 		"""
# 	self.values = []
    
# 	while head:
#         self.values.append(head.val)
#         head = head.next

# 	def getRandom(self) -> int:
# 	"""
# 		Returns a random node's value.
# 		"""
# 	import random 
# 	return random.choice(self.values)


#kadane's theory for linear max subarray solution 
def max_subarray(A):
    max_ending_here = max_so_far = A[0]

    for x in A[1:]: 
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far

listOfStrings2 = ['Hi' for i in range(20)]

prac_arr = ["hi" for _ in range(10)]

#print(max_subarray([1, 5, -1, 0, 10]))
# print(prac_arr)

# from collections import Counter

# ans = Counter()
# for num in [1,2,2]:
#     ans[num] += 1


# print(ans)


# for i in xrange(len(frags)):
#     ans[".".join(frags[i:])] += count 

#     ans[".".join(frags[i:])] += count

from collections import Counter 

def canPermutePalindrome(s):
    word_count = Counter()
    odd_cnt = 0

    for char in s:
        word_count[char] += 1

    for key, val in word_count.items():
        if (val % 2) != 0:
            odd_cnt += 1     
        if odd_cnt > 1:
            return False 

    return True


print(canPermutePalindrome("aabbcq"))


# public class Solution {
#     public int findLHS(int[] nums) {
#         HashMap < Integer, Integer > map = new HashMap < > ();
#         int res = 0;
#         for (int num: nums) {
#             map.put(num, map.getOrDefault(num, 0) + 1); }
#         for (int key: map.keySet()) {
#             if (map.containsKey(key + 1))
#             res = Math.max(res, map.get(key) + map.get(key + 1));}
#         return res; }
# }
