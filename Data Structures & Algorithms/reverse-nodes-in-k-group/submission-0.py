class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Reverse every complete group of k
        for i in range(0, len(arr), k):
            if i + k <= len(arr):
                arr[i:i+k] = arr[i:i+k][::-1]

        # Copy values back
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1

        return head