class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1,1

        for n in nums:
            tmp = n*curMax
            curMax = max(n, n*curMax, n*curMin)
            curMin = min(n, tmp, n*curMin)

            res = max(res, curMax)
        return res
        