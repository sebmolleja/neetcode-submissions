# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = 0
        self.kth = 0

        def dfs(node, k):
            if not node or self.kth == k:
                return

            left = dfs(node.left, k)

            self.kth += 1
            if self.kth == k:
                self.smallest = node.val

            right = dfs(node.right, k)

        dfs(root, k)
        return self.smallest
            
