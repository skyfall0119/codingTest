# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isnodegood(self, node:TreeNode, max_num):
        if not node:
            return
        
        if node.val >= max_num:
            self.cnt_good += 1
            
        max_num = max(max_num, node.val)

        self.isnodegood(node.left, max_num)
        self.isnodegood(node.right, max_num)

    def goodNodes(self, root: TreeNode) -> int:
        self.cnt_good = 1
        self.isnodegood(root.left, root.val)
        self.isnodegood(root.right, root.val)
        return self.cnt_good
        
        