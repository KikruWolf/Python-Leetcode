class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key in a:
                a[key].append(i) 
            else:
                a[key] = [i]
        return a.values()

# Sort each word alphabetically to get a shared key for all its anagrams.
# Group words into a dictionary using that key, then return the groups.
# Time: O(n * m) | Space: O(n)