# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def dfs(left, right):
            if left > right:
                return None

            node = TreeNode(preorder[self.preorder_idx])
            mid = inorder_map[node.val]
            self.preorder_idx += 1

            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node
        
        return dfs(0, len(inorder) - 1)


        