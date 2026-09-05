class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                i, v = stack.pop()
                res[i] = ind - i
            stack.append([ind, val])
        return res
        