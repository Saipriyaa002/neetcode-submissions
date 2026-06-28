class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[]
        for n in nums:
            if n!=val:
                l.append(n)
        for i in range(len(l)):
            nums[i] = l[i]
        a=len(l)
        return a