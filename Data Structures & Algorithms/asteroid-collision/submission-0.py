class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for a in asteroids:
            while s and a<0 and s[-1]>0:
                d=a+s[-1]
                if d<0:
                    s.pop()
                elif d>0:
                    a=0
                else:
                    s.pop()
                    a=0
            if a:
                s.append(a)
        return s