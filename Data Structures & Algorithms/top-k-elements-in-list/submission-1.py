class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for n in nums:
            f[n]=f.get(n,0)+1
        f=dict(sorted(f.items(),key=lambda x: x[1],reverse=True))
        a=[]
        for keys in f:
            a.append(keys)
            if len(a)==k:
                break
        return a