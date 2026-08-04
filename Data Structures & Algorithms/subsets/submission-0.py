class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def dfs(ind,p):
            if ind==len(nums):
                a.append(p[:])
                return
                
            p.append(nums[ind])

            dfs(ind+1,p)
            p.pop()
            dfs(ind+1,p)
        dfs(0,[])
        return a 