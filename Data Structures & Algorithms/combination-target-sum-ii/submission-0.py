class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        a=[]
        def dfs(s,p,r):
            if r==0:
                a.append(p[:])
                return
            
            for i in range(s,len(candidates)):
                if i > s and candidates[i]==candidates[i-1]:
                    continue
                if r<candidates[i]:
                    break
                p.append(candidates[i])
                dfs(i+1,p,r-candidates[i])
                p.pop()
        dfs(0,[],target)
        return a