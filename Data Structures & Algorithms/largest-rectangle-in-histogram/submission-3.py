class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #When we see a taller/equal bar: keep going
        #When we see a shorter bar:
        #"The taller bars cannot continue anymore."
        #Pop them
        #Calculate their areas
        #Remember how far left the new shorter bar can extend

        stack = []
        maxA = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                ind, val = stack.pop()
                maxA = max(maxA, val * (i-ind))
                start = ind
            stack.append([start, v])
        
        for i, v in stack:
            maxA = max(maxA, v * (len(heights) - i))
        return maxA




        