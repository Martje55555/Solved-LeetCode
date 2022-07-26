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
        map = {}
        
        curr = head
        index = 0
        while curr:
            if curr in map:
                return curr
            else:
                map[curr] = index
                index += 1
            curr = curr.next
        return None