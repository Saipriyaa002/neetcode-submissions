# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''d=ListNode(0)
        d.next=head
        f=d
        s=d
        for _ in range(n):
            f=f.next
        while f.next:
            f=f.next
            s=s.next
        s.next=s.next.next
        return d.next'''
        d=ListNode(0,head)
        l=d
        r=head
        while n>0 and r:
            r=r.next
            n-=1
        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return d.next

