class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1] :
                ind, val = stack.pop()
                res[ind] = i - ind
            stack.append([i,temperatures[i]])
        return res


        