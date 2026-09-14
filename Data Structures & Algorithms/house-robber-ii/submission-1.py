class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        
    def helper(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        two = nums[0]
        one = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = one
            one = max(one, nums[i]+two)
            two = temp
        return one