class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        max=0
        for p in prices:
            if (p<min):
                min=p
            d=p-min
            if(d>max):
                max=d
        return max