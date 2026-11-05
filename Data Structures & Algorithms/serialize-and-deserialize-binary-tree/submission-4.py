# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []

        def dfs(node):
            if not node:
                self.result.append("N")
                return
            
            self.result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)
        return ",".join(self.result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.index = 0

        def dfs():
            val = values[self.index]
            self.index += 1

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()






    """
    serialize: 
    preorder traversal to array of each node.val
    when node.val == None append N
    join array to string with , to get final 1,2,N,N,3,4,N,N,5,N,N

    deserialize:
    values = data.split(",")



    """
