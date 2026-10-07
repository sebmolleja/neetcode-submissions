# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


        


    

    """
        if p and q are less than curr root then LCA must be in the left 
        if p and q greater than curr root then LCA must be in right

        other wise we have LCA but two cases: 

        1. they split - one to th eleft one to the right
        2. root is p or q and the other is left or right

    """
        
