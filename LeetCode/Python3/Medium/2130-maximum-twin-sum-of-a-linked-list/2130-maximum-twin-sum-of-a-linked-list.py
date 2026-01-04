# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if head is None:
            return 0

        q = deque([head])
        while head.next:
            head = head.next
            q.append(head)

        max_sum = 0
        while q:
            temp_sum = q.popleft().val + q.pop().val
            max_sum = max(temp_sum, max_sum)
        
        return max_sum
