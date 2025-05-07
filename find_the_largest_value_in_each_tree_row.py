# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
            

            if not root :
                return []
            queue = deque([root])  
            large = []       
            while queue:
                level_size = len(queue)
                largest =  float('-inf')
                for _ in range(level_size) :
                    node = queue.popleft()
                    largest = max(largest,node.val)
                    if node.left :
                        queue.append(node.left)
                    if node.right :
                        queue.append(node.right)
                large.append(largest)
            return large


             
