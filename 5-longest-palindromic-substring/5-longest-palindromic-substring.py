class Solution(object):
    def longestPalindrome(self, s):
        def findPalinIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        
        start, end = 0,0
        
        for i in range(len(s)):
            evenLeft, evenRight = findPalinIndex(s, i, i+1)
            oddLeft, oddRight = findPalinIndex(s, i, i)
            
            if evenRight - evenLeft > end - start:
                start, end = evenLeft, evenRight
            if oddRight - oddLeft > end - start:
                start, end = oddLeft, oddRight
                
        return s[start : end+1]
        