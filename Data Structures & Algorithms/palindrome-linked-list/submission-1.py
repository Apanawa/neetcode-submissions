# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        array = []

        while node:
            array.append(node.val)
            node = node.next
        
        l = 0
        r = len(array) - 1
        while l < r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1
        return True
        