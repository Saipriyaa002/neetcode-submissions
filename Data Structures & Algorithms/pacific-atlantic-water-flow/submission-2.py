class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        p=set()
        a=set()
        def dfs(i,j,v):
            if (i,j) in v:
                return
            v.add((i,j))
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<r and 0<=y<c:
                    if heights[x][y]>=heights[i][j]:
                        dfs(x,y,v)
        for i in range(r):
            dfs(i,0,p)
        for j in range(c):
            dfs(0,j,p)
        for i in range(r):
            dfs(i,c-1,a)
        for j in range(c):
            dfs(r-1,j,a)
        ans = []

        for i in range(r):
            for j in range(c):
                if (i, j) in p and (i, j) in a:
                    ans.append([i, j])

        return ans