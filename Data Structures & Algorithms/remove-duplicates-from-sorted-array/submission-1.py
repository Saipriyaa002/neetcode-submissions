class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]    

        for c in nums:
            if c not in l:
                l.append(c)
            
        nums[:]=l
        return len(l)