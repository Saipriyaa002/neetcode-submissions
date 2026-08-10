class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=[]
        c=head
        while c:
            a.append(c.val)
            c=c.next
        for i in range(0,len(a),k):
            if i+k<=len(a):
                a[i:i+k]=a[i:i+k][::-1]
        c=head
        i=0
        while c:
            c.val=a[i]
            c=c.next
            i+=1
        return head