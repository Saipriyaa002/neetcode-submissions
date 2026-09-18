class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        t=0
        a=float('inf')
        for r in range(len(nums)):
            t+=nums[r]
            while t>=target:
                a=min(a,r-l+1)
                t-=nums[l]
                l+=1
        return 0 if a==float('inf') else a