import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f={}
        l=[]
        for n in nums:
            f[n]=f.get(n,0)+1
        for key in f:
            if f[key]>len(nums)//3:
                l.append(key)
        return l