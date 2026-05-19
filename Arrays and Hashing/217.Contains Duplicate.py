class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set()
        for i in nums:
            if i not in x:
                x.add(i)
            else:
                return True
        return False

# Approach: iterate through nums once, tracking seen values in a set.
# Set lookup is O(1), so we can check and add in a single pass.
# Time: O(n) | Space: O(n)
#
# Alternative: sort first (O(n log n)), then check adjacent elements.
# Duplicates will always be neighbours after sorting.
# Time: O(n log n) | Space: O(1) — better on space, worse on time.

# Another alternative Solution, self-explanitory

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)