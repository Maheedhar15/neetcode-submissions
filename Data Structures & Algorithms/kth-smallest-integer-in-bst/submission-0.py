# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# To find the Kth Smallest, Recursively travel the BST in InOrder format and return the value at the Kth posn
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.result = None
        def dfs(root):
            
            if root == None or self.result is not None:
                return 
            dfs(root.left)
            self.cnt+=1
            if self.cnt == k:
                self.result = root.val
                return
            
            dfs(root.right)
        dfs(root)
        return self.result
            
                

