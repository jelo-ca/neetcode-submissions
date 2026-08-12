# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        return self.reverse(None, head)

    
    def reverse(self, prev, curr):
        if curr is None:
            return prev

        temp = curr.next # 1

        curr.next = prev # 0 > null
        prev = curr # 0

        return self.reverse(prev, temp) # 0, 1

        # return prev
