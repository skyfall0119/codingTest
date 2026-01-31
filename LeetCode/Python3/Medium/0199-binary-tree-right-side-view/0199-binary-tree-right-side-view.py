from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([(root,0)])

        res = {}

        while q:
            cur, lv = q.popleft()
            if cur is None:
                continue

            res[lv] = cur.val
            q.append((cur.left, lv+1))
            q.append((cur.right, lv+1))


        temp = list(res.items())
        temp.sort(key= lambda x: x[0])
        return [y for x,y in temp]