'''class Solution:
    def countSubstrings(self, s: str) -> int:
        a=[]
        c=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                a.append(s[i:j])
        for i in a:
            if i==i[::-1]:
                c+=1
        return c'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # Even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count