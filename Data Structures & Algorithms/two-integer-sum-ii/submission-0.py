class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            for  j in range(i,n):
                if numbers[i]+numbers[j]==target:
                    return [numbers[i],numbers[j]]