# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        pre=None
        cur=s.next
        s.next=None
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        fir=head
        sec=pre
        while sec:
            t1=fir.next
            t2=sec.next
            fir.next=sec
            sec.next=t1
            fir=t1
            sec=t2
