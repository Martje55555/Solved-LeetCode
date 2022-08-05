class Solution(object):
    def twoSum(self, nums, target):
        diff = {}
        
        for i, num in enumerate(nums):
            if target - num in diff:
                return [i, diff[target-num]]
            else:
                diff[num] = i
        
        return []
        
        