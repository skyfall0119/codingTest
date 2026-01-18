# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzag(self, node:TreeNode, isLeft:bool, cnt:int):
        if not node:
            return

        self.max_cnt = max(cnt, self.max_cnt)

        if isLeft: 
            self.zigzag(node.right, False, cnt+1)
            self.zigzag(node.left, True, 1)
        else:
            self.zigzag(node.left, True, cnt+1)
            self.zigzag(node.right, False, 1)


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_cnt = 0

        self.zigzag(root.left, True, 1)
        self.zigzag(root.right, False, 1)

        return self.max_cnt