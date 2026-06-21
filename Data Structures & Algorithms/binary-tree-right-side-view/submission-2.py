# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#    Traverse by the level, and return the last element
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(root):
            level_elements = {}
            q = deque()
             
            if root:
                q.append(root)
            level = 0
            while len(q) > 0:
                for i in range(len(q)):
                    curr = q.popleft()
                    if level not in level_elements:
                        level_elements[level] = [curr.val]
                    else:
                        level_elements[level].append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                level+=1
            return level_elements
        level_elements = bfs(root)
        for i in level_elements:
            res.append(level_elements[i][-1])
        return res


        