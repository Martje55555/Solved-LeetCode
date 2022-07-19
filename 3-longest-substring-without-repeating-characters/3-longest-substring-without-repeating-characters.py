class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        start = 0
        longest = 0
        
        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
            seen[s[i]] = i
            longest = max(longest, i-start + 1)
        return longest
        