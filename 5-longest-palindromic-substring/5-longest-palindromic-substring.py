class Solution(object):
    def longestPalindrome(self, s):
        def findPalinIndex(s, l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        
        start, end = 0,0
        
        for i in range(len(s)):
            oddLeft, oddRight = findPalinIndex(s, i, i)
            evenLeft, evenRight = findPalinIndex(s, i, i+1)
            
            if oddRight - oddLeft > end - start:
                start, end = oddLeft, oddRight
            if evenRight - evenLeft > end - start:
                start, end = evenLeft, evenRight
        
        return s[start : end+1]
        