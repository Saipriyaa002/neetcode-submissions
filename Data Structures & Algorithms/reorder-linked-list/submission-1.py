# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f=s=head
        while f and f.next:
            s=s.next
            f=f.next.next
        p=None
        c=s.next
        s.next=None
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        fir=head
        sec=p
        while sec:
            t1=fir.next
            t2=sec.next
            fir.next=sec
            sec.next=t1
            fir=t1
            sec=t2
        