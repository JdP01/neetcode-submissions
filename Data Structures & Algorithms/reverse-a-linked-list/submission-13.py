# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None: 
            return head
        
        prev = None
        current = head

        while current: 
            next = current.next
            current.next = prev
            prev = current
            current = next

        next2 = current
        while not next2 == None: 
            print(next2.val)
            next2 = next2.next

        return prev