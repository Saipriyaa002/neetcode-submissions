class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        n=len(heights)
        l=0
        r=n-1
        while l<r:
            b=min(heights[l],heights[r])*(r-l)
            a=max(a,b)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return a