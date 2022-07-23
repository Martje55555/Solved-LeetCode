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
        prev = None
        next = None
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev   
    
    '''
    curr = 1
    prev = None
    next = None
    
    1st iteration
    next = 2
    curr.next = None
    prev = 1
    curr = 2
    
    2nd iteration
    next = 3
    curr.next = 1
    prev = 2
    curr = 3
    
    3rd iteration
    next = 4
    curr.next = 2
    prev = 3
    curr = 4
    
    4th iteration
    next = 5
    curr.next = 3
    prev = 4
    curr = 5
    
    5th iteration
    next = None
    curr.next = 4
    prev = 5
    curr = None
    
    Done
    
    outcome: print(prev)
    [5, 4, 3, 2, 1]
    '''