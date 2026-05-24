# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []

        currA = headA
        currB = headB

        while currA:
            stackA.append(currA)
            currA = currA.next

        while currB:
            stackB.append(currB)
            currB = currB.next

        ans = None

        while stackA and stackB:
            if stackA[-1] == stackB[-1]:
                ans = stackA[-1]
                stackA.pop()
                stackB.pop()
            else:
                break

        return ans
