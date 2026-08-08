class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        a=0
        u=d=0
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                u=d+1
                d=1
            elif arr[i]<arr[i-1]:
                d=u+1
                u=1
            else:
                u=d=1
            a=max(a,d,u)
        return a