class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def ss(p,ind):
            if ind==len(nums):
                a.append(p[:])
                return
            p.append(nums[ind])
            ss(p,ind+1)
            p.pop()
            ss(p,ind+1)
        ss([],0)
        return a