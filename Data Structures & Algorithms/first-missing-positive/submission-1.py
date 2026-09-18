class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m=1
        for n in nums:
            if n<m:
                continue
            elif n==m:
                m+=1
            else:
                return m
        return m