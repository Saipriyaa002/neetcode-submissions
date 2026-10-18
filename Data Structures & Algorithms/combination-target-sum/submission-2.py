class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        def cs(i,p,t):
            if t==target:
                a.append(p[:])
                return
            if i==len(nums) or t>target:
                return
            p.append(nums[i])
            cs(i,p,t+nums[i])
            p.pop()
            cs(i+1,p,t)
        cs(0,[],0)
        return a