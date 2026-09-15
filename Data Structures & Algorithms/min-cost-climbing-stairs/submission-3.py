class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        one, two = 0,0
        for i in range(2, n+1):
            temp = two
            two = min(one+cost[i-2], two+cost[i-1])
            one = temp
        return two
        