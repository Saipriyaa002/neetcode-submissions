class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        #m=0
        n=len(nums)
        for a in nums:
            c[a]=c.get(a,0)+1
        for i in c:
            if c[i]>n/2:
                return i
        #return i