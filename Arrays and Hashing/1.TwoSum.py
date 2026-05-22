class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# For each number, calculate its complement (target - num) and check if seen before.
# Store each number and its index as we go so complements can be looked up in O(1).
# Time: O(n) | Space: O(n)