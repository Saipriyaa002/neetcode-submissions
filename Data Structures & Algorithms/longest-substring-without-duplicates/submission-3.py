class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        l=0
        se=set()
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            a=max(a,r-l+1)
        return a