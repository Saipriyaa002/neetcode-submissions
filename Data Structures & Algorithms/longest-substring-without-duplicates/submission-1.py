class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        l=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            a=max(a,i-l+1)
        return a
