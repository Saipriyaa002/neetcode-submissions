class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=1
        h=x
        a=0
        while l<=h:
            m=(l+h)//2
            if m*m==x:
                return m
            elif m*m<x:
                a=m
                l=m+1
            else:
                h=m-1
        return a