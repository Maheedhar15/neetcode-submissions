# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if root == None:
                return 0,True
        
            leftHeight, isLeftBalanced = checkBalance(root.left)
            if not isLeftBalanced:
                return 0, False
            rightHeight, isRightBalanced = checkBalance(root.right)
            if not isRightBalanced:
                return 0, False

            isCurrentBalanced = abs(leftHeight - rightHeight) <= 1

            return max(leftHeight,rightHeight) + 1, isCurrentBalanced
        _, isBalanced = checkBalance(root)
        return isBalanced