class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        e = dict()
        e2 = dict()
        if len(s) == len(t): 
            for letter in s:
                if letter not in e:
                    e[letter] = 1
                else:
                    e[letter] += 1
            for letter in t:
                if letter not in e2:
                    e2[letter] = 1
                else:
                    e2[letter] += 1
            if e == e2:
                return True
            return False
        else:
            return False

# Count frequency of each letter in both strings using two dictionaries.
# Early exit if lengths differ. Compare dictionaries directly.
# Time: O(n) | Space: O(n)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x='abcdefghijklmnopqrstuvwxyz'
        for i in x:
            if s.count(i)!=t.count(i):
                return False
        return True

# Loop through the alphabet and check each letter's count in both strings.
# Simpler but only works for lowercase English letters, not Unicode.
# Time: O(n) | Space: O(1)