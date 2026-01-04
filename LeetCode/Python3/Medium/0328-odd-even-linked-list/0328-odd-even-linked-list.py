# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        # even, odd starting point
        even, odd = ListNode(), ListNode()
        even_cur, odd_cur = even, odd
        
        is_odd = True
        
        # split even and odd nodes 
        while cur:
            if is_odd:
                odd_cur.next = cur
                cur = cur.next
                odd_cur = odd_cur.next
                is_odd = False
            else:
                even_cur.next = cur
                cur = cur.next
                even_cur = even_cur.next
                is_odd = True
        
        odd_cur.next = even.next
        even_cur.next = None
        return odd.next
        