# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ''
        def preorder(root):
            if root == None:
                self.res+='null,'
                return ''
            self.res+=f"{str(root.val)},"
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return self.res[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.split(',')

        print(nodes)

        def helper(nodes):
            if nodes == None:
                return None
            
            val = nodes.pop(0)
            if val == "null":
                return None
            
            root = TreeNode(int(val))
            root.left = helper(nodes)
            root.right = helper(nodes)
            return root
        
        return helper(nodes)

