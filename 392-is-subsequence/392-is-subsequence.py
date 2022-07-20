class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        
        if len(s) > len(t):
            return False
        
        curr = 0
        for i in range(len(t)):
            if t[i] == s[curr]:
                curr += 1
                if curr == len(s):
                    return True
        return False
        