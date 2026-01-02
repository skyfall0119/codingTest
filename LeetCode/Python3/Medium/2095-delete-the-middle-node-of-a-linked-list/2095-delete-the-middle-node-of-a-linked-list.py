# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next is None:
            return None

        move = 0
        mid = head
        cur = head
        while cur.next:
            if move == 2:
                move = 0
                mid = mid.next
                
            cur = cur.next
            move += 1
            
        
        mid.next = mid.next.next

        return head
