# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])

        dic = defaultdict(int)

        while q:
            cur, lv = q.popleft()

            if cur is None:
                continue

            dic[lv] += cur.val
            q.append((cur.left, lv+1))
            q.append((cur.right, lv+1))

        return max(dic, key=dic.get)

            
