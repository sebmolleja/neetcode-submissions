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
            self.preorder_idx += 1
            mid = inorder_map[node.val]

            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node
        
        return dfs(0, len(inorder) - 1)
    


    """
    preorder = [1,2,3,4], inorder = [2,1,3,4]


    


    """
        