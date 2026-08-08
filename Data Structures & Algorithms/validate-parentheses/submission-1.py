class Solution:
    def isValid(self, s: str) -> bool:
        s=[]
        pairs={')':'(','}':'{',']':'['}
        for i in s:
            if i in '[{(':
                s.append(i)
            else:
                if not s or s[-1]!=pairs[ch]:
                    return False
                    s.pop()
                
        return len(s)==0