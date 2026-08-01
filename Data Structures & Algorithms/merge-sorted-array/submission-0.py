class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = nums1[:m]
        n2 = nums2[:n]

        a = []

        l = r = 0

        while l < len(n1) and r < len(n2):
            if n1[l] < n2[r]:
                a.append(n1[l])
                l += 1
            else:
                a.append(n2[r])
                r += 1

        while l < len(n1):
            a.append(n1[l])
            l += 1

        while r < len(n2):
            a.append(n2[r])
            r += 1

        nums1[:] = a
        