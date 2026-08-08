class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s=[0]*(n+1)
        for a,b in scores:
            s[a]-=1
            s[b]+=1
        for i in range(1,n+1):
            if s[i]==n-1:
                return i
        return -1