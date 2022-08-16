class Solution(object):
    def longestPalindrome(self, s):
        def findIndex(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        
        start, end = 0,0
        
        for i in range(len(s)):
            oddLeft, oddRight = findIndex(s, i, i)
            evenLeft, evenRight = findIndex(s, i, i+1)
            
            if end - start < oddRight - oddLeft:
                start, end = oddLeft, oddRight
            if end - start < evenRight - evenLeft:
                start, end = evenLeft, evenRight
        
        return s[start : end+1]
                
        