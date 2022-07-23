# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = 0
        temp = head
        
        while temp is not None:
            temp = temp.next
            size += 1
        
        mid = size // 2
        
        curr = head
        
        for i in range(mid):
            curr = curr.next
        
        return curr
        