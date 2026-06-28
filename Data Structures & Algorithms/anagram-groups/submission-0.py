class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        v=[False]*len(strs)
        for i in range(len(strs)):
            if v[i]:
                continue
            g=[strs[i]]
            v[i]=True
            for j in range(i+1,len(strs)):
                if not v[j] and sorted(strs[i])==sorted(strs[j]):
                    g.append(strs[j])
                    v[j]=True
            l.append(g)
        return l