class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def ss(p,i):
            if i==len(nums):
                a.append(p[:])
                return
            p.append(nums[i])
            ss(p,i+1)
            p.pop()
            ss(p,i+1)
        ss([],0)
        return a