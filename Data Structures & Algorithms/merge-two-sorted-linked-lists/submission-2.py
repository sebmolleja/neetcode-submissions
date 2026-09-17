# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                nxt_val = curr1
                tail.next = nxt_val
                tail = tail.next
                curr1 = curr1.next
            else:
                nxt_val = curr2
                tail.next = nxt_val
                tail = tail.next
                curr2 = curr2.next

        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        
        return dummy.next
