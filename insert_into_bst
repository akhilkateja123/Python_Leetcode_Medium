class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return None
        
        if val>root.val:
            if root.right is None:
                root.right= TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        
        else:
            if root.left is None:
                root.left= TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        
        return root
        
