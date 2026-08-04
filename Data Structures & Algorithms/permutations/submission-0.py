class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ls=[]
        def perm(nums,l,r):
            if l==r:
                ls.append(nums[:])
                return
            for i in range(l,r+1):
                nums[i],nums[l]=nums[l],nums[i]
                perm(nums,l+1,r)
                nums[i],nums[l]=nums[l],nums[i]
        l=0
        r=len(nums)-1
        perm(nums,l,r)
        return ls