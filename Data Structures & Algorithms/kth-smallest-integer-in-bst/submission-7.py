# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = 0
        self.node_count = 0

        def dfs(node):
            if not node or self.node_count == k:
                return

            dfs(node.left)

            self.node_count += 1
            if self.node_count == k:
                self.smallest = node.val
            
            dfs(node.right)
        
        dfs(root)
        return self.smallest


        