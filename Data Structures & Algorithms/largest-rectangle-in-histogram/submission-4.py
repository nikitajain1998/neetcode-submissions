class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxA = 0

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                ind, val = stack.pop()
                maxA = max(maxA,val * (i-ind))
                start = ind
            stack.append([start,v])
        
        for i, v in stack:
            maxA = max(maxA, v * (len(heights) - i))
        
        return maxA
        