class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #two pointers with sort, not works for unsorted array
        # i = 0
        # j = len(nums)-1
        # while i < j:
        #     if (nums[i] + nums[j]) == target:
        #         return [i,j]
        #     elif (nums[i] + nums[j]) > target:
        #         j = j-1
        #     elif (nums[i] + nums[j]) < target:
        #         i = i + 1

        #hashtable
        count = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in count:
                return [count[comp],i]
            count[nums[i]] = i

        