class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        a=[]
        ph={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        def dfs(ind,p):
            if ind==len(digits):
                a.append("".join(p))
                return
            for ch in ph[digits[ind]]:
                p.append(ch)
                dfs(ind+1,p)
                p.pop()
        dfs(0,[])
        return a
