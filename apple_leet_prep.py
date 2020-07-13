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
