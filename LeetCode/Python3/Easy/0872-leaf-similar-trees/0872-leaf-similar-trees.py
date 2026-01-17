

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q1 = [root1]
        q2 = [root2]

        q1_list = []
        while q1:
            r = q1.pop()
            if r is None:
                continue
            if not r.left and not r.right:
                q1_list.append(r.val)
                continue

            if r.right:
                q1.append(r.right)
            if r.left:
                q1.append(r.left)

        q2_list = []
        while q2:
            r = q2.pop()
            if r is None:
                continue
            if not r.left and not r.right:
                q2_list.append(r.val)
                continue

            if r.right:
                q2.append(r.right)
            if r.left:
                q2.append(r.left)
        
        return tuple(q1_list) == tuple(q2_list)
        