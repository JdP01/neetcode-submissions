# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return None
        
        if not root.left and not root.right:
            return root
        #if root.left.left and root.left.right and root.right.left and root.right.right: # if both children are leaves
            #swap children directly

        left_child = self.invertTree(root.left)
        right_child = self.invertTree(root.right)

        root.left = right_child
        root.right = left_child

        return root