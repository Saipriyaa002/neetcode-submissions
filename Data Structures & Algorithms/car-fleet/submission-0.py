class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        lt=0
        f=0
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        for c in cars:
            p=c[0]
            s=c[1]
            t=(target-p)/s
            if t>lt:
                f=f+1
                lt=t
        return f
            