# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        curr = head
        while curr and curr.next:
            curr.val = sys.maxint
            if curr.next.val == sys.maxint:
                return curr.next
            curr = curr.next
            
        return None