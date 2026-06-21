# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        first = head
        while(list1!=None and list2!=None):
            
            if list1.val <= list2.val:
                if head:
                    print(head.val)
                    curr = list1
                    list1 = list1.next
                    head.next = curr
                    head = head.next
                    
                else:
                    curr = list1
                    list1 = list1.next
                    head = curr
                    first = head
            else:
                if head:
                    print(head.val)
                    curr = list2
                    list2 = list2.next
                    head.next = curr
                    head = head.next
                else:
                    curr = list2
                    list2 = list2.next
                    head = curr
                    first = head

        if list1 == None and list2 != None:
            if head:
                head.next = list2
            else:
                head = list2
                first = head
        if list2 == None and list1 != None:
            if head:
                head.next = list1
            else:
                head = list1
                first = head
        
        return first

        