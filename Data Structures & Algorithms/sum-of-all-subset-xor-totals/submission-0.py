class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        a=0
        def dfs(i,xor):
            nonlocal a
            if i==len(nums):
                a+=xor
                return
            
            dfs(i+1,xor^nums[i])
            dfs(i+1,xor)
        dfs(0,0)
        return a