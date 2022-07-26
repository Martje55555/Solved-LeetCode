# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        exists = []
        
        curr = head
        while curr:
            if curr in exists:
                return curr
            else:
                exists.append(curr)
            curr = curr.next
        return None