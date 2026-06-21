# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = float('-inf')
        def dfs(root):
            if root == None:
                return -1
            leftDepth = 1 + dfs(root.left)
            rightDepth = 1 + dfs(root.right)
            self.maxDepth = max(self.maxDepth, leftDepth + rightDepth)
            return max(leftDepth, rightDepth)
        dfs(root)
        return self.maxDepth

        