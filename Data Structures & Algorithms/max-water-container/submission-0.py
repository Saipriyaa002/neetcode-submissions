class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        n=len(heights)
        for i in range(n):
            for j in range(i+1,n):
                a=min(heights[i],heights[j])*(j-i)
                ans=max(a,ans)
        return ans