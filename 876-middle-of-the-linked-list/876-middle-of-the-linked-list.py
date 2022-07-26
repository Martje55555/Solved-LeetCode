# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        tortoise = head
        hare = head
        
        while hare and hare.next != None:
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise