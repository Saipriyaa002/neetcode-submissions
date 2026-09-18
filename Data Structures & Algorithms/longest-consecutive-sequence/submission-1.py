class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest=0
        s=set(nums)
        for n in s:
            if n-1 not in s:
                c=n
                l=1
                while c+1 in s:
                    c+=1
                    l+=1
                longest=max(l,longest)
        return longest