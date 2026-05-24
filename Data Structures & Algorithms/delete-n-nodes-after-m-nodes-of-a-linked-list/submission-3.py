# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        last = head
        while curr:
            cutA = m
            cutB = n
            while curr and cutA != 0:
                last = curr
                curr = curr.next
                cutA -= 1
            while cutB != 0 and curr:
                curr = curr.next
                cutB -= 1
            last.next = curr
        return head

