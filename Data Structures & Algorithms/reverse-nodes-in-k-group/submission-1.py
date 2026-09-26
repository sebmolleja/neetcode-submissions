# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_end = kth.next
            group_start = group_prev.next
            self.reverse(group_start, group_end)

            group_prev.next = kth
            group_prev = group_start


    def reverse(self, start, end):
        prev = end
        curr = start

        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            

