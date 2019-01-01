class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        
        max_val= max(nums)
        node= TreeNode(max_val)
        max_index= nums.index(max_val)
        
        node.left= self.constructMaximumBinaryTree(nums[:max_index])
        node.right= self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return node
        
