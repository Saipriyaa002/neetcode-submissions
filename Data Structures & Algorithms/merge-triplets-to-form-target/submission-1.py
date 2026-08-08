class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f=[False,False,False]
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]:
                f[0]=True
            if b == target[1]:
                f[1] = True
            if c == target[2]:
                f[2] = True
        return all(f)
