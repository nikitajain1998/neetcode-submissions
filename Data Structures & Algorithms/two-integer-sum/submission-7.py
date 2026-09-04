class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in count:
                return[count[comp], i]
            count[nums[i]] = i

        