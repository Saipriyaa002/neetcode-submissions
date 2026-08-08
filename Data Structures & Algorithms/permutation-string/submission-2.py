class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if need == window:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if need == window:
                return True

        return False'''
        a=[]
        def permute(s,l,r):
            if l==r:
                a.append("".join(s))
                return
            for i in range(l,r+1):
                s[i],s[l]=s[l],s[i]
                permute(s,l+1,r)
                s[i],s[l]=s[l],s[i]
        l=0
        r=len(s1)-1
        b=[]
        for ch in s1:
            b.append(ch)
        permute(b,l,r)
        for i in a:
            if i in s2:
                return True
        return False