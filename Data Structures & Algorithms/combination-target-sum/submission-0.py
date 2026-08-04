class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        def dfs(ind,p,t):
            if t==target:
                a.append(p[:])
                return
            if ind==len(nums) or t>target:
                return
            p.append(nums[ind])
            dfs(ind,p,t+nums[ind])
            p.pop()
            dfs(ind+1,p,t)
        
        dfs(0,[],0)
        return a