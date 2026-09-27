"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clones = {None : None}

        curr = head
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = clones[curr]
            copy.next = clones[curr.next]
            copy.random = clones[curr.random]
            curr = curr.next

        return clones[head]

        
    """
    clones {
        Node(3, 7, null) : Node(3)
        Node(7, 4, 5) : Node(7)

    }

    """

        