class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dct:
                return [i, dct[diff]]
            else:
                dct[num] = i