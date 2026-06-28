class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        for p in path.split('/'):
            if p==''or p=='.':
                continue
            elif p=="..":
                if s:
                    s.pop()
            else:
                s.append(p)
        return '/'+'/'.join(s)
                