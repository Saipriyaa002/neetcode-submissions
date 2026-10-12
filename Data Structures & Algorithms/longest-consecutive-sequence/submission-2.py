class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        long=0
        s=set(nums)
        for n in s:
            if n-1 not in s:
                c=n
                l=1
                while c+1 in s:
                    c+=1
                    l+=1
                long=max(l,long)
        return long