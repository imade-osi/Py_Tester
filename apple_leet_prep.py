# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

       # # 1 -> 2 -> 3 -> 4 -> 5
       #   ^
       # # 1 <- 2 <- 3 <- 4 <- 5

        prev = None
        curr = head

        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev


#given [2,3,-1,2,4,8], target = 0
#         ^
#output  [[1,2,3], [2,3,4], [3,2,1]]


#novice solution

#start at first index of arr
#iterate through array for values after first index
# perform two sum operations on sub array
# collect triplet into return array if found
# move onto next index in outer loop


def find_unique_triplets(arr, target):

    trip_hash = {}

    for outer_ele in arr:

        for inner in

    return []
