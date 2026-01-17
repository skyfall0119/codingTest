# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        stk = [(root, 1)]

        if root is None:
            return 0
        
        while stk:
            cur, depth = stk.pop()
            max_depth = max(max_depth, depth)
            
            if not cur:
                return

            if cur.left:
                stk.append((cur.left, depth+1))
            if cur.right:
                stk.append((cur.right, depth+1))
        return max_depth