class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = list(bin(start)[2:])
        y = list(bin(goal)[2:])

        if len(x)>len(y):
            y = ((len(x)-len(y))*["0"]) + y
        if len(y)>len(x):
            x = ((len(y)-len(x))*["0"]) + x
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        return c
        
