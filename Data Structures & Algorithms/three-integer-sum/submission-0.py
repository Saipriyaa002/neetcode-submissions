class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        s=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (nums[i]+nums[j]+nums[k]==0):
                        tr=list(sorted([nums[i],nums[j],nums[k]]))
                        if tr not in l:
                            l.append(tr)
        return l