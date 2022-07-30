class Solution(object):
    def longestPalindrome(self, s):
        
        def findPalIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            oddLeft, oddRight = findPalIndex(s, i, i)
            evenLeft, evenRight = findPalIndex(s, i, i+1)
            
            if oddRight - oddLeft > end - start:
                end = oddRight
                start = oddLeft
            if evenRight - evenLeft > end - start:
                end = evenRight
                start = evenLeft
                
        return s[start : end+1]
            