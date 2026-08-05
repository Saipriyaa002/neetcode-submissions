class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]

        def dfs(s,p):
            a.append(p[:])

            for i in range(s,len(nums)):
                if i>s and nums[i]==nums[i-1]:
                    continue
                p.append(nums[i])
                dfs(i+1,p)
                p.pop()
        dfs (0,[])
        return a