# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        
        curr = head
        next = None
        prev = None
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        