class Solution(object):
    def findDifferentBinaryString(self, nums):
        bits = len(nums[0])

        exists = set(int(num, 2) for num in nums)

        for num in range(2 ** bits):
            if num not in exists:
                get_bin = lambda x, n: format(x, 'b').zfill(n)
                return get_bin(num, bits)