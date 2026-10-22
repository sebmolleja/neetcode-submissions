# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        slow.next = None
        left = head
        right = prev

        while left and right:
            left_nxt = left.next
            right_nxt = right.next

            left.next = right
            right.next = left_nxt

            left = left_nxt
            right = right_nxt

            




        


    """
    [2,4,5,6,8,9]
           ^
               ^
    
    [2,4,5,6,8,9]



    




    """


        