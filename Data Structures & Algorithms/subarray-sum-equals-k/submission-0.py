class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if s==k:
                    c+=1
        return c