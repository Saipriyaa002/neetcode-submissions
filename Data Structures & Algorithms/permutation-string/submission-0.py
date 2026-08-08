class Solution:
    def permute(self,s, l, r, ans):
        if l == r:
            ans.append("".join(s))
            return

        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            self.permute(s, l + 1, r, ans)
            s[l], s[i] = s[i], s[l]

    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans=[]
        ch=list(s1)
        self.permute(ch, 0, len(ch) - 1, ans)
        for i in ans:
            if i in s2:
                return True
        return False
