class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        #c=0
        for n in operations:
            if n in "123456789":
                s.append(int(n))
            elif n == "+":
                a=s.pop()
                b=s.pop()
                c=a+b
                s.append(int(b))
                s.append(int(a))
                s.append(int(c))
            elif n=="C":
                s.pop()
            else:
                a=s.pop()
                b=a*2
                s.append(int(a))
                s.append(int(b))
        return sum(s)