class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c=[]
        lt=0
        f=0
        for i in range(len(position)):
            c.append([position[i],speed[i]])
        c.sort(reverse=True)
        for a in c:
            p=a[0]
            s=a[1]
            t=(target-p)/s
            if t>lt:
                lt=t
                f+=1
        return f  