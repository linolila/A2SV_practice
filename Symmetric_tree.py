# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left_sub,right_sub):
            if not left_sub and not right_sub :
                return True
            if left_sub is None or right_sub is None or left_sub.val!= right_sub.val:
                return False
            return isMirror(left_sub.left,right_sub.right) and isMirror(left_sub.right,right_sub.left)
        if root is None:
            return True 
        return isMirror(root.left,root.right)
