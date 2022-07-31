class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return 1
        newSet = set()
        
        for i in range(len(s)):
            if s[i] in newSet:
                newSet.remove(s[i])
            else:
                newSet.add(s[i])
        if len(newSet) <= 1 : return len(s)
        
        return len(s) - len(newSet) + 1