class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ls=[]
        def perm(nums,l,r):
            s=set()
            if l==r:
                ls.append(nums[:])
                return
            for i in range(l,r+1):
                if nums[i] in s:
                    continue
                s.add(nums[i])
                nums[i],nums[l]=nums[l],nums[i]
                perm(nums,l+1,r)
                nums[i],nums[l]=nums[l],nums[i]
        l=0
        r=len(nums)-1
        perm(nums,l,r)
        ls.sort()
        return ls