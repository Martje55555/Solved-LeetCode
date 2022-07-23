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
        tortoise = head
        hare = head
        
        while hare and hare.next != None:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise