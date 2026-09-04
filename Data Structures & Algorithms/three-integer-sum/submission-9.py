class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for ind, val in enumerate(nums):
            if val > 0:
                break
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue
            l, r = ind + 1, len(nums)-1
            while l < r:
                sum = val + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l +=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res
        