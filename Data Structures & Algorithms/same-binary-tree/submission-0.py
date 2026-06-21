# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root1, root2):
            q1, q2 = deque([root1]), deque([root2])

            while q1 and q2:
                curr1 = q1.popleft()
                curr2 = q2.popleft()

                # If one is None and the other is not, trees differ
                if not curr1 and not curr2:
                    continue
                if not curr1 or not curr2:
                    return False

                # If values differ, trees differ
                if curr1.val != curr2.val:
                    return False

                # Enqueue left and right children for both nodes
                q1.append(curr1.left)
                q1.append(curr1.right)
                q2.append(curr2.left)
                q2.append(curr2.right)
            return not q1 and not q2
        
        return bfs(p,q)

        