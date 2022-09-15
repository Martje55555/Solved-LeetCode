class Solution(object):
    def twoSum(self, nums, target):
        differences = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in differences: return [differences[diff], i]
            else: differences[num] = i
        return []