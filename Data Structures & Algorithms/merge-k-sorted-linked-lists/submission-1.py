# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        for head in lists:
            while head:
                a.append(head.val)
                head=head.next
            if not a:
                return None
        a.sort()
        d=ListNode(0)
        c=d
        for n in a:
            c.next=ListNode(n)
            c=c.next
        return d.next