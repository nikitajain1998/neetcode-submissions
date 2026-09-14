class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = 0, 0
        for i in range(2, n+1):
            temp = one
            one = min(one+cost[i-1] , two+cost[i-2])
            two = temp
        
        return one
        