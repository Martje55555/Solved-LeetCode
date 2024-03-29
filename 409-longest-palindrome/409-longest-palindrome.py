class Solution(object):
    def longestPalindrome(self, s):
        
        if len(s) == 1:
            return 1
        
        hold = set()
        
        for i in range(len(s)):
            if s[i] in hold:
                hold.remove(s[i])
            else:
                hold.add(s[i])
                                
        if bool(len(hold) < 1):
            return len(s)
        
        return len(s) - len(hold) + 1