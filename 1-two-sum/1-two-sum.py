class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in dict:
                return [dict[difference], i]
            else:
                dict[nums[i]] = i
        return []
                