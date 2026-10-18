class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=[]
        def p(s,l,r):
            if l==r:
                a.append(s[:])
                return
            for i in range(l,r+1):
                s[i],s[l]=s[l],s[i]
                p(s,l+1,r)
                s[i],s[l]=s[l],s[i]
        l=0
        r=len(nums)-1
        p(nums,l,r)
        return a        