class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        q=deque()
        f=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    f+=1
        t=0
        while q and f>0:
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<r and 0<=y<c and grid[x][y]==1:
                        grid[x][y]=2
                        f-=1
                        q.append((x,y))
            t+=1
        if f>0:
            return -1
        return t