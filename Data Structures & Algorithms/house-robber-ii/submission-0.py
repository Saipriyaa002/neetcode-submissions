class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(nums):
            a = 0
            b = 0

            for x in nums:
                a, b = b, max(b, a + x)

            return b

        return max(solve(nums[:-1]), solve(nums[1:]))