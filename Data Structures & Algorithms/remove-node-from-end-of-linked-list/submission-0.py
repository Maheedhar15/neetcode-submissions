# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        curr = head

        while curr:
            length+=1
            curr = curr.next

        diff = length - n - 1

        if diff == -1:
            return head.next

        temp = 0

        curr = head

        while curr:
            if temp == diff:
                curr.next = curr.next.next
                break
            temp+=1
            curr = curr.next
        
        return head

        